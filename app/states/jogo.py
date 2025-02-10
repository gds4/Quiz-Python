import pygame
import random
from components.BotaoQuiz import BotaoQuiz 
from database.database import get_db 
from service.questao_service import QuestaoService
from states.fim_de_jogo import FimDeJogo
from config import PRETO, BRANCO, NEUTRA, AZUL, CINZA_ESCURO

class Jogo:
    TEMPO_PERGUNTA = 15 
    DELAY_POS_RESPOSTA = 1000

    def __init__(self, game):
        self.game = game

        db = next(get_db())
        self.questao_service = QuestaoService(db)
        self.questoes = self.questao_service.obter_questoes_aleatorias()
        
        self.indice_pergunta = 0
        self.pontuacao = 0

        self.font_pergunta = pygame.font.Font(None, 36)
        self.font_resposta = pygame.font.Font(None, 32)
        self.font_info = pygame.font.Font(None, 28)

        self.alternativas = []
        self.carregar_pergunta_atual()

        self.tempo_inicio = pygame.time.get_ticks()
        self.resposta_selecionada = False
        self.tempo_resposta = None

        self.efeito_sonoro_acertou = pygame.mixer.Sound("app/assets/sounds/alternativa-correta.mp3")
        self.efeito_sonoro_errou = pygame.mixer.Sound("app/assets/sounds/alternativa-errada.mp3")

    def carregar_pergunta_atual(self):
        if self.indice_pergunta < len(self.questoes):
            self.pergunta_atual = self.questoes[self.indice_pergunta]
            alternativas = list(self.pergunta_atual.respostas)
            random.shuffle(alternativas)
            self.alternativas = []

            x = 50
            y_inicial = 300
            largura = self.game.tela.get_width() - 100
            altura = 60
            espacamento = 20

            for i, alt in enumerate(alternativas):
                btn = BotaoQuiz(
                    x=x,
                    y=y_inicial + i * (altura + espacamento),
                    largura=largura,
                    altura=altura,
                    fonte=self.font_resposta,
                    texto=alt.texto,
                    cor_texto=PRETO,
                    resposta=alt
                )
                self.alternativas.append(btn)

            self.tempo_inicio = pygame.time.get_ticks()
            self.resposta_selecionada = False
            self.tempo_resposta = None
        else:
            self.game.mudar_tela(FimDeJogo(self.game, self.pontuacao))

    def capturar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.executando = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not self.resposta_selecionada:
                    for btn in self.alternativas:
                        if btn.verificar_colisao():
                            acertou = btn.marcar_resposta()
                            self.resposta_selecionada = True
                            self.tempo_resposta = pygame.time.get_ticks()
                            
                            tempo_decorrido = (self.tempo_resposta - self.tempo_inicio) / 1000
                            tempo_restante = max(0, self.TEMPO_PERGUNTA - tempo_decorrido)
                            
                            if acertou:
                                self.pontuacao += int(tempo_restante * 10)
                                self.efeito_sonoro_acertou.play()
                            else:
                                self.efeito_sonoro_errou.play()
                            break

    def atualizar(self):
        for btn in self.alternativas:
            btn.atualizar()

        tempo_atual = pygame.time.get_ticks()

        if not self.resposta_selecionada:
            tempo_esgotou = (tempo_atual - self.tempo_inicio) / 1000 >= self.TEMPO_PERGUNTA
            if tempo_esgotou:
                self.resposta_selecionada = True
                self.tempo_resposta = tempo_atual
        else:
            if tempo_atual - self.tempo_resposta >= self.DELAY_POS_RESPOSTA:
                self.indice_pergunta += 1
                self.carregar_pergunta_atual()

    def desenhar(self):
        sombra_rect = pygame.Rect(28, 58, self.game.tela.get_width() - 56, 184)
        pergunta_rect = pygame.Rect(30, 60, self.game.tela.get_width() - 60, 180)
        
        pygame.draw.rect(self.game.tela, CINZA_ESCURO, sombra_rect, border_radius=15)  # Sombra
        pygame.draw.rect(self.game.tela, AZUL, pergunta_rect, border_radius=15)
        pygame.draw.rect(self.game.tela, BRANCO, pergunta_rect, width=2, border_radius=15)  # Contorno
        
        largura_max = self.game.tela.get_width() - 100
        linhas_pergunta = quebrar_texto(self.pergunta_atual.pergunta, self.font_pergunta, largura_max)
        
        y_pergunta = 100
        for linha in linhas_pergunta:
            texto_pergunta = self.font_pergunta.render(linha, True, BRANCO)
            rect_pergunta = texto_pergunta.get_rect(center=(self.game.tela.get_width() // 2, y_pergunta))
            self.game.tela.blit(texto_pergunta, rect_pergunta)
            y_pergunta += 35  

        for btn in self.alternativas:
            btn.desenhar(self.game.tela)

        tempo_decorrido = (pygame.time.get_ticks() - self.tempo_inicio) / 1000
        tempo_restante = max(0, int(self.TEMPO_PERGUNTA - tempo_decorrido))
        texto_tempo = self.font_info.render(f"Tempo: {tempo_restante}", True, PRETO)
        self.game.tela.blit(texto_tempo, (50, 20))

        texto_pontos = self.font_info.render(f"Pontuação: {self.pontuacao}", True, PRETO)
        self.game.tela.blit(texto_pontos, (self.game.tela.get_width() - 200, 20))

        self.game.desenhar_mouse()

def quebrar_texto(texto, fonte, largura_max):
    palavras = texto.split()
    linhas = []
    linha_atual = ""

    for palavra in palavras:
        teste_linha = linha_atual + " " + palavra if linha_atual else palavra
        largura_teste, _ = fonte.size(teste_linha)

        if largura_teste <= largura_max:
            linha_atual = teste_linha
        else:
            linhas.append(linha_atual)
            linha_atual = palavra

    if linha_atual:
        linhas.append(linha_atual)

    return linhas