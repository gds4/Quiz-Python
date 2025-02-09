import random
import pygame
import socket
import json
import threading
from components.BotaoQuiz import BotaoQuiz
from states.fim_de_jogo import FimDeJogo
from config import PRETO


SERVER_IP = "localhost"  # Altere para o IP do servidor se necessário
SERVER_PORT = 7777

class JogoMultiplayer:
    TEMPO_PERGUNTA = 15 
    DELAY_POS_RESPOSTA = 1000

    def __init__(self, game):
        self.game = game
        self.questoes = []  # Lista para armazenar as questões recebidas do servidor
        self.indice_pergunta = 0
        self.pontuacao = 0

        self.font_pergunta = pygame.font.Font(None, 36)
        self.font_resposta = pygame.font.Font(None, 30)
        self.font_info = pygame.font.Font(None, 28)

        # Cria os botões de alternativas para a pergunta atual
        self.alternativas = []
        
        # Flag para indicar que as questões já foram carregadas
        self.questoes_carregadas = False

        # Inicia uma thread para conectar ao servidor e buscar as questões
        self.network_thread = threading.Thread(target=self.connect_to_server)
        self.network_thread.daemon = True  # Assim, essa thread não impede o encerramento do programa
        self.network_thread.start()

        # Controla o tempo da pergunta
        self.tempo_inicio = pygame.time.get_ticks()
        self.resposta_selecionada = False  # Flag que indica que uma resposta foi dada
        self.tempo_resposta = None  # Momento em que a resposta foi selecionada

    def connect_to_server(self):
        """Conecta ao servidor e obtém as questões de forma assíncrona."""
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((SERVER_IP, SERVER_PORT))
            print("Conectado ao servidor, aguardando perguntas...")

            # Aguarda as perguntas do servidor (essa chamada é bloqueante, mas está em outra thread)
            data = json.loads(self.client_socket.recv(4096).decode())
            if data["type"] == "questoes":
                self.questoes = data["dados"]  # Armazena as questões recebidas do servidor
                print("Questões recebidas:", self.questoes)
                self.questoes_carregadas = True
        except Exception as e:
            print("Erro na conexão:", e)
            # Se ocorrer um erro, você pode mudar para o menu ou tratar conforme necessário
            self.cancelar_busca_jogadores()

    def cancelar_busca_jogadores(self):
        """Cancela a busca por jogadores e retorna para o menu."""
        print("Cancelando busca por jogadores...")
        try:
            self.client_socket.close()
        except Exception as e:
            print("Erro ao fechar socket:", e)
        from states.menu import Menu
        self.game.mudar_tela(Menu(self.game))

    def finalizar_partida(self):
        """Envia a pontuação para o servidor após a partida."""
        data = json.dumps({"type": "pontuacao", "pontuacao": self.pontuacao})
        self.client_socket.send(data.encode())
        
        # Aguarda o servidor retornar a pontuação do adversário
        data = json.loads(self.client_socket.recv(4096).decode())
        if data["type"] == "resultado":
            print("Resultado final recebido: ", data["pontuacoes"])
            self.game.mudar_tela(FimDeJogo(self.game, self.pontuacao, data["pontuacoes"]))
            
        # Encerra a conexão depois que o resultado for recebido
        self.client_socket.close()

    def carregar_pergunta_atual(self):
        """Carrega a pergunta atual e cria os botões para as alternativas."""
        if self.indice_pergunta < len(self.questoes):
            self.pergunta_atual = self.questoes[self.indice_pergunta]
            # Embaralha as alternativas para não ficar sempre na mesma ordem
            alternativas = self.pergunta_atual['respostas']  # As respostas vêm do dicionário da questão
            random.shuffle(alternativas)
            self.alternativas = []

            # Define posições para os botões (exemplo: 4 alternativas dispostas verticalmente)
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
                    texto=alt['texto'],  # Exibe o texto da resposta
                    cor_texto=PRETO,
                    resposta=alt  # Pode ser um dicionário ou objeto, conforme sua implementação
                )
                self.alternativas.append(btn)

            # Reinicia o timer da pergunta
            self.tempo_inicio = pygame.time.get_ticks()
            self.resposta_selecionada = False
            self.tempo_resposta = None
        else:
            print("Não há mais perguntas, finalizando partida.")
            self.finalizar_partida()

    def capturar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.executando = False

            if event.type == pygame.KEYDOWN:
                # Se o usuário pressionar ESC, cancela a busca e retorna para o menu
                if event.key == pygame.K_ESCAPE:
                    self.cancelar_busca_jogadores()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not self.resposta_selecionada:
                    pos = pygame.mouse.get_pos()
                    for btn in self.alternativas:
                        if btn.verificar_click(pos):
                            # Marca a resposta e calcula pontos se a resposta for correta
                            acertou = btn.marcar_resposta()
                            self.resposta_selecionada = True
                            self.tempo_resposta = pygame.time.get_ticks()
                            
                            # Calcula o tempo decorrido em segundos (resposta rápida gera mais pontos)
                            tempo_decorrido = (self.tempo_resposta - self.tempo_inicio) / 1000
                            tempo_restante = max(0, self.TEMPO_PERGUNTA - tempo_decorrido)
                            
                            if acertou:
                                self.pontuacao += int(tempo_restante * 10)
                            break

    def atualizar(self):
        # Atualiza os botões das alternativas
        for btn in self.alternativas:
            btn.atualizar()

        tempo_atual = pygame.time.get_ticks()
        if not self.resposta_selecionada:
            tempo_esgotou = (tempo_atual - self.tempo_inicio) / 1000 >= self.TEMPO_PERGUNTA
            if tempo_esgotou:
                self.resposta_selecionada = True
                self.tempo_resposta = tempo_atual
        else:
            # Se uma resposta já foi selecionada ou o tempo acabou, espera um delay para ir para a próxima pergunta
            if tempo_atual - self.tempo_resposta >= self.DELAY_POS_RESPOSTA:
                self.indice_pergunta += 1
                self.carregar_pergunta_atual()

        # Se as questões já foram carregadas e ainda não foi definida a pergunta atual, carrega a primeira
        if self.questoes_carregadas and not hasattr(self, 'pergunta_atual'):
            self.carregar_pergunta_atual()

    def desenhar(self):
        if not self.questoes_carregadas:
            # Enquanto espera por outro jogador, exibe mensagem de espera com opção de cancelar
            mensagem = "Aguardando outro jogador...\n(Pressione ESC para cancelar)"
            # Dividindo em duas linhas para renderizar de forma adequada:
            linhas = mensagem.split("\n")
            y = self.game.tela.get_height() // 2 - 20
            for linha in linhas:
                texto_espera = self.font_pergunta.render(linha, True, PRETO)
                rect = texto_espera.get_rect(center=(self.game.tela.get_width() // 2, y))
                self.game.tela.blit(texto_espera, rect)
                y += 40
        else:
            if hasattr(self, 'pergunta_atual'):
                largura_max = self.game.tela.get_width() - 100
                linhas_pergunta = quebrar_texto(self.pergunta_atual['pergunta'], self.font_pergunta, largura_max)

                y_pergunta = 80
                for linha in linhas_pergunta:
                    texto_pergunta = self.font_pergunta.render(linha, True, PRETO)
                    rect_pergunta = texto_pergunta.get_rect(center=(self.game.tela.get_width() // 2, y_pergunta))
                    self.game.tela.blit(texto_pergunta, rect_pergunta)
                    y_pergunta += 30  

                for btn in self.alternativas:
                    btn.desenhar(self.game.tela)

                tempo_decorrido = (pygame.time.get_ticks() - self.tempo_inicio) / 1000
                tempo_restante = max(0, int(self.TEMPO_PERGUNTA - tempo_decorrido))
                texto_tempo = self.font_info.render(f"Tempo: {tempo_restante}", True, PRETO)
                self.game.tela.blit(texto_tempo, (50, 20))

                texto_pontos = self.font_info.render(f"Pontuação: {self.pontuacao}", True, PRETO)
                self.game.tela.blit(texto_pontos, (self.game.tela.get_width() - 200, 20))
            else:
                # Se por algum motivo as questões foram carregadas mas a pergunta atual não foi definida,
                # tenta carregar a primeira pergunta.
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
