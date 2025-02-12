import pygame
import random
import socket
import json
import threading
from components.BotaoQuiz import BotaoQuiz 
from pages.fim_de_jogo import FimDeJogo
from config import PRETO, BRANCO, AZUL, CINZA_ESCURO, SERVER_IP, SERVER_PORT

class Jogo:
    TEMPO_PERGUNTA = 15 
    DELAY_POS_RESPOSTA = 1000
    SERVIDOR_HOST = SERVER_IP
    SERVIDOR_PORTA = SERVER_PORT

    def __init__(self, game):
        self.game = game

        # Inicialmente, não temos questões; elas serão carregadas via thread.
        self.questoes = []
        self.indice_pergunta = 0
        self.pontuacao = 0
        self.questoes_carregadas = False  # Indica quando a conexão já terminou (com sucesso ou não)
        self.connection_failed = False    # Indica se houve erro na conexão
        self.conectando = True            # Enquanto True, estamos tentando nos conectar

        self.font_pergunta = pygame.font.Font(None, 36)
        self.font_resposta = pygame.font.Font(None, 32)
        self.font_info = pygame.font.Font(None, 28)

        self.alternativas = []

        self.tempo_inicio = None
        self.resposta_selecionada = False
        self.tempo_resposta = None

        self.efeito_sonoro_acertou = pygame.mixer.Sound("app/assets/sounds/alternativa-correta.mp3")
        self.efeito_sonoro_errou = pygame.mixer.Sound("app/assets/sounds/alternativa-errada.mp3")

        # Inicia a thread para conectar com o servidor sem bloquear o jogo.
        self.network_thread = threading.Thread(target=self.connect_to_server)
        self.network_thread.daemon = True
        self.network_thread.start()

    def connect_to_server(self):
        """
        Tenta conectar ao servidor para obter as questões.
        Se a conexão for bem-sucedida, atualiza self.questoes e seta questoes_carregadas.
        Caso contrário, seta connection_failed e questoes_carregadas para que o sistema
        exiba a mensagem de erro e permita cancelar.
        """
        try:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.connect((self.SERVIDOR_HOST, self.SERVIDOR_PORTA))
            
            mensagem = json.dumps({"type": "singleplayer"})
            cliente.send(mensagem.encode())
            
            resposta = cliente.recv(4096)
            cliente.close()
            
            dados = json.loads(resposta.decode())
            if "dados" in dados:
                self.questoes = dados["dados"]
            else:
                self.questoes = []
            self.conectando = False
            self.questoes_carregadas = True
        except Exception as e:
            print("Erro ao obter perguntas do servidor:", e)
            self.conectando = False
            self.connection_failed = True
            self.questoes_carregadas = True

    def cancelar_conexao(self):
        """
        Método chamado quando o jogador pressiona ESC para cancelar a conexão.
        Normalmente, esse método muda a tela para o Menu.
        """
        print("Cancelando conexão com o servidor...")
        from pages.menu import Menu 
        self.game.mudar_tela(Menu(self.game))

    def carregar_pergunta_atual(self):
        if self.indice_pergunta < len(self.questoes):
            self.pergunta_atual = self.questoes[self.indice_pergunta]
            alternativas = list(self.pergunta_atual["respostas"])
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
                    texto=alt["texto"],
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

            # Em qualquer momento (seja enquanto conecta ou durante o jogo) o jogador pode pressionar ESC para cancelar.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.cancelar_conexao()

            # Somente processa eventos de clique se as questões já estiverem carregadas e não houver erro de conexão.
            if self.questoes_carregadas and not self.connection_failed:
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
        # Se as questões ainda não foram carregadas, não atualiza nada.
        if not self.questoes_carregadas:
            return
        if self.connection_failed:
            return

        # Se ainda não carregamos a primeira pergunta, faça isso.
        if not hasattr(self, 'pergunta_atual'):
            self.carregar_pergunta_atual()
            # É importante retornar aqui para evitar usar tempo_inicio imediatamente
            # antes de atualizar a interface.
            return

        # Atualiza os botões
        for btn in self.alternativas:
            btn.atualizar()

        tempo_atual = pygame.time.get_ticks()
        if not self.resposta_selecionada:
            # Aqui self.tempo_inicio já foi definido em carregar_pergunta_atual()
            tempo_esgotou = (tempo_atual - self.tempo_inicio) / 1000 >= self.TEMPO_PERGUNTA
            if tempo_esgotou:
                self.resposta_selecionada = True
                self.tempo_resposta = tempo_atual
        else:
            if tempo_atual - self.tempo_resposta >= self.DELAY_POS_RESPOSTA:
                self.indice_pergunta += 1
                self.carregar_pergunta_atual()


        # Caso as questões tenham sido carregadas, mas ainda não foi iniciada a primeira pergunta,
        # carrega-a.
        if self.questoes_carregadas and not hasattr(self, 'pergunta_atual'):
            self.carregar_pergunta_atual()

    def desenhar(self):
        # Se as questões ainda não foram carregadas, exibe mensagem de conexão.
        if not self.questoes_carregadas:
            mensagem = self.font_info.render("Tentando se conectar...", True, PRETO)
            rect = mensagem.get_rect(center=(self.game.tela.get_width() // 2,
                                             self.game.tela.get_height() // 2))
            self.game.tela.blit(mensagem, rect)
            mensagem2 = self.font_info.render("(Pressione ESC para cancelar)", True, PRETO)
            rect2 = mensagem2.get_rect(center=(self.game.tela.get_width() // 2,
                                               self.game.tela.get_height() // 2 + 40))
            self.game.tela.blit(mensagem2, rect2)
            self.game.desenhar_mouse()
            return
        # Se houve erro na conexão, exibe mensagem de erro.
        elif self.connection_failed:
            mensagem = self.font_info.render("Erro ao conectar ao servidor.", True, PRETO)
            rect = mensagem.get_rect(center=(self.game.tela.get_width() // 2,
                                             self.game.tela.get_height() // 2))
            self.game.tela.blit(mensagem, rect)
            mensagem2 = self.font_info.render("Pressione ESC para cancelar", True, PRETO)
            rect2 = mensagem2.get_rect(center=(self.game.tela.get_width() // 2,
                                               self.game.tela.get_height() // 2 + 40))
            self.game.tela.blit(mensagem2, rect2)
            self.game.desenhar_mouse()
            return

        # Caso contrário, desenha a interface normal do jogo.
        sombra_rect = pygame.Rect(28, 58, self.game.tela.get_width() - 56, 184)
        pergunta_rect = pygame.Rect(30, 60, self.game.tela.get_width() - 60, 180)
        
        pygame.draw.rect(self.game.tela, CINZA_ESCURO, sombra_rect, border_radius=15)  # Sombra
        pygame.draw.rect(self.game.tela, AZUL, pergunta_rect, border_radius=15)
        pygame.draw.rect(self.game.tela, BRANCO, pergunta_rect, width=2, border_radius=15)  # Contorno
        
        largura_max = self.game.tela.get_width() - 100
        linhas_pergunta = quebrar_texto(self.pergunta_atual["pergunta"], self.font_pergunta, largura_max)
        
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
