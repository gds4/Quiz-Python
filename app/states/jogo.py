import pygame
import random
from components.BotaoQuiz import BotaoQuiz 
from database.database import get_db 
from service.questao_service import QuestaoService
from states.fim_de_jogo import FimDeJogo
from config import BRANCO, PRETO

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
        self.font_resposta = pygame.font.Font(None, 30)
        self.font_info = pygame.font.Font(None, 28)

        # Cria os botões de alternativas para a pergunta atual
        self.alternativas = []
        self.carregar_pergunta_atual()

        # Controla o tempo da pergunta
        self.tempo_inicio = pygame.time.get_ticks()
        self.resposta_selecionada = False  # Flag que indica que uma resposta foi dada
        self.tempo_resposta = None  # Momento em que a resposta foi selecionada

    def carregar_pergunta_atual(self):
        """Carrega a pergunta atual e cria os botões para as alternativas."""
        if self.indice_pergunta < len(self.questoes):
      
            self.pergunta_atual = self.questoes[self.indice_pergunta]
            # Embaralha as alternativas para não ficar sempre na mesma ordem
            alternativas = list(self.pergunta_atual.respostas)
            random.shuffle(alternativas)
            self.alternativas = []

            # Define posições para os botões (exemplo: 4 alternativas dispostas verticalmente)
            x = 50
            y_inicial = 200
            largura = self.game.tela.get_width() - 100
            altura = 50
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
                    resposta=alt  # objeto Resposta
                )
                self.alternativas.append(btn)

            # Reinicia o timer da pergunta
            self.tempo_inicio = pygame.time.get_ticks()
            self.resposta_selecionada = False
            self.tempo_resposta = None
        else:
            # Se não há mais perguntas, muda para a tela de fim de jogo
            self.game.mudar_tela(FimDeJogo(self.game, self.pontuacao))

    def capturar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.executando = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not self.resposta_selecionada:
                    pos = pygame.mouse.get_pos()
                    for btn in self.alternativas:
                        if btn.verificar_click(pos) and event.button == 1:
                            # Marca a resposta e calcula pontos se a resposta for correta
                            acertou = btn.marcar_resposta()
                            self.resposta_selecionada = True
                            self.tempo_resposta = pygame.time.get_ticks()
                            
                            # Calcula o tempo decorrido em segundos (resposta rápida gera mais pontos)
                            tempo_decorrido = (self.tempo_resposta - self.tempo_inicio) / 1000
                            tempo_restante = max(0, self.TEMPO_PERGUNTA - tempo_decorrido)
                            
                            # Exemplo de cálculo de pontos: 10 pontos por segundo restante
                            if acertou:
                                self.pontuacao += int(tempo_restante * 10)
                            break

    def atualizar(self):
        # Atualiza os botões das alternativas
        for btn in self.alternativas:
            btn.atualizar()

        tempo_atual = pygame.time.get_ticks()

        if not self.resposta_selecionada:
            # Verifica se o tempo da pergunta esgotou
            if (tempo_atual - self.tempo_inicio) / 1000 >= self.TEMPO_PERGUNTA:
                self.resposta_selecionada = True
                self.tempo_resposta = tempo_atual
                # Nenhum ponto é somado se o tempo acabar
        else:
            # Se uma resposta já foi selecionada ou o tempo acabou, espera um delay para ir para a próxima pergunta
            if tempo_atual - self.tempo_resposta >= self.DELAY_POS_RESPOSTA:
                self.indice_pergunta += 1
                self.carregar_pergunta_atual()

    def desenhar(self):
        self.game.tela.fill(BRANCO)

        # Exibe a pergunta atual
        texto_pergunta = self.font_pergunta.render(self.pergunta_atual.pergunta, True, PRETO)
        rect_pergunta = texto_pergunta.get_rect(center=(self.game.tela.get_width() // 2, 100))
        self.game.tela.blit(texto_pergunta, rect_pergunta)

        # Desenha os botões das alternativas
        for btn in self.alternativas:
            btn.desenhar(self.game.tela)

        # Desenha informações: tempo restante e pontuação
        tempo_decorrido = (pygame.time.get_ticks() - self.tempo_inicio) / 1000
        tempo_restante = max(0, int(self.TEMPO_PERGUNTA - tempo_decorrido))
        texto_tempo = self.font_info.render(f"Tempo: {tempo_restante}", True, PRETO)
        self.game.tela.blit(texto_tempo, (50, 20))

        texto_pontos = self.font_info.render(f"Pontuação: {self.pontuacao}", True, PRETO)
        self.game.tela.blit(texto_pontos, (self.game.tela.get_width() - 200, 20))

        self.game.desenhar_mouse()
