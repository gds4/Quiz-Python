import random
import pygame
import socket
import json
import threading
from components.BotaoQuiz import BotaoQuiz
from pages.fim_de_jogo_multiplayer import FimDeJogoMultiplayer
from config import PRETO, BRANCO, AZUL, CINZA_ESCURO, SERVER_IP, SERVER_PORT

class JogoMultiplayer:
    TEMPO_PERGUNTA = 15
    DELAY_POS_RESPOSTA = 1000

    def __init__(self, game):
        self.game = game
        self.questoes = [] 
        self.indice_pergunta = 0
        self.pontuacao = 0

        self.font_pergunta = pygame.font.Font(None, 32)
        self.font_resposta = pygame.font.Font(None, 30)
        self.font_info = pygame.font.Font(None, 28)

        self.alternativas = []      
        self.questoes_carregadas = False
        self.aguardando_resultado = False 
        self.player_id = None      

        self.socket_fechado = False 

        self.network_thread = threading.Thread(target=self.connect_to_server)
        self.network_thread.daemon = True
        self.network_thread.start()

        self.tempo_inicio = pygame.time.get_ticks()
        self.resposta_selecionada = False
        self.tempo_resposta = None

    def connect_to_server(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((SERVER_IP, SERVER_PORT))
            
            self.client_socket.send(json.dumps({"type": "multiplayer"}).encode())
            
            data = json.loads(self.client_socket.recv(4096).decode())
            if data["type"] == "questoes":
                self.questoes = data["dados"]
                self.player_id = data.get("player", "p1")
                print("Questões recebidas:", self.questoes, "Você é:", self.player_id)
                self.questoes_carregadas = True
        except Exception as e:
            print("Erro na conexão:", e)
            self.cancelar_busca_jogadores()

    def cancelar_busca_jogadores(self):
        print("Cancelando busca por jogadores...")
        self.fechar_socket()
        from pages.menu import Menu
        self.game.mudar_tela(Menu(self.game))

    def fechar_socket(self):

        if not self.socket_fechado:
            try:
                self.client_socket.close()
            except Exception as e:
                print("Erro ao fechar socket:", e)
            self.socket_fechado = True

    def finalizar_partida(self):
        try:
            data = json.dumps({"type": "pontuacao", "pontuacao": self.pontuacao})
            self.client_socket.send(data.encode())
        except Exception as e:
            print("Erro ao enviar pontuação:", e)
        
        self.aguardando_resultado = True
        resultado_thread = threading.Thread(target=self.aguardar_resultado)
        resultado_thread.daemon = True
        resultado_thread.start()

    def aguardar_resultado(self):
        try:
            result_data = self.client_socket.recv(4096)
            if result_data:
                result = json.loads(result_data.decode())
                if result.get("type") == "resultado":
                    scores = result.get("pontuacoes", {})
                    if self.player_id is None:
                        self.player_id = "p1"
                    if self.player_id == "p1":
                        adversario_score = scores.get("p2", 0)
                    else:
                        adversario_score = scores.get("p1", 0)
                    self.game.mudar_tela(FimDeJogoMultiplayer(self.game, self.pontuacao, adversario_score))
        except Exception as e:
            print("Erro ao aguardar resultado:", e)

    def carregar_pergunta_atual(self):
        if self.indice_pergunta < len(self.questoes):
            self.pergunta_atual = self.questoes[self.indice_pergunta]
            alternativas = self.pergunta_atual['respostas']
            random.shuffle(alternativas)
            self.alternativas = []

            x = 50
            y_inicial = 300
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
                    texto=alt['texto'],
                    cor_texto=PRETO,
                    resposta=alt
                )
                self.alternativas.append(btn)

            self.tempo_inicio = pygame.time.get_ticks()
            self.resposta_selecionada = False
            self.tempo_resposta = None
        else:
            self.finalizar_partida()

    def capturar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.executando = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.cancelar_busca_jogadores()
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
                                self.game.efeito_sonoro_acertou.play()
                            else:
                                self.game.efeito_sonoro_errou.play()
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

        if self.questoes_carregadas and not hasattr(self, 'pergunta_atual'):
            self.carregar_pergunta_atual()

    def desenhar(self):
        if self.aguardando_resultado:
            waiting_msg = self.font_info.render("Aguardando adversário finalizar...", True, PRETO)
            rect = waiting_msg.get_rect(center=(self.game.tela.get_width() // 2,
                                                self.game.tela.get_height() // 2))
            self.game.tela.blit(waiting_msg, rect)
            self.game.desenhar_mouse()
            return

        if not self.questoes_carregadas:
            mensagem = "Aguardando outro jogador...\n(Pressione ESC para cancelar)"
            linhas = mensagem.split("\n")
            y = self.game.tela.get_height() // 2 - 20
            for linha in linhas:
                texto_espera = self.font_pergunta.render(linha, True, PRETO)
                rect = texto_espera.get_rect(center=(self.game.tela.get_width() // 2, y))
                self.game.tela.blit(texto_espera, rect)
                y += 40
        else:
            if hasattr(self, 'pergunta_atual'):
                sombra_rect = pygame.Rect(28, 58, self.game.tela.get_width() - 56, 184)
                pergunta_rect = pygame.Rect(30, 60, self.game.tela.get_width() - 60, 180)
                
                pygame.draw.rect(self.game.tela, CINZA_ESCURO, sombra_rect, border_radius=15)  # Sombra
                pygame.draw.rect(self.game.tela, AZUL, pergunta_rect, border_radius=15)
                pygame.draw.rect(self.game.tela, BRANCO, pergunta_rect, width=2, border_radius=15)  # Contorno
                
                largura_max = self.game.tela.get_width() - 100
                linhas_pergunta = quebrar_texto(self.pergunta_atual['pergunta'], self.font_pergunta, largura_max)
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
            else:
                self.carregar_pergunta_atual()

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
