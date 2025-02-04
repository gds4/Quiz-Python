import pygame
import sys
from components.Botao import Botao 
from config import BRANCO, PRETO, LARGURA_TELA, ALTURA_TELA

class Menu:
    def __init__(self, game):
        self.game = game  # Referência ao jogo principal
        self.fonte = pygame.font.Font(None, 48)
        self.botaoJogar = Botao(x=80, y=250, largura=200, altura=50, cor_botao=BRANCO, fonte=self.fonte, texto='Jogar', cor_texto = PRETO)
        self.botaoSair = Botao(x=80, y=320, largura=200, altura=50, cor_botao=BRANCO, fonte=self.fonte, texto='Sair', cor_texto = PRETO)
        self.imagem_fundo = pygame.image.load('app/assets/gradiente_verde_azul.png')
        self.imagem_fundo = pygame.transform.scale(self.imagem_fundo, (LARGURA_TELA, ALTURA_TELA))

    def capturar_eventos(self):
        """Captura eventos do teclado."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.executando = False
                pygame.quit()
                sys.exit()
    def atualizar(self):
        """Atualiza a lógica do menu (se necessário)."""
        pass

    def desenhar(self):
        #Desenha o menu na tela
        self.game.tela.blit(self.imagem_fundo,(0,0))
        self.botaoJogar.desenhar(self.game.tela)
        self.botaoSair.desenhar(self.game.tela)
        
