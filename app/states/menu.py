import pygame
import sys
from components.Botao import Botao 
from config import BRANCO, PRETO

class Menu:
    def __init__(self, game):
        self.game = game  # Referência ao jogo principal
        self.fonte = pygame.font.Font(None, 48)
        self.botao = Botao(x=300, y=250, largura=200, altura=50, cor_botao=BRANCO, fonte=self.fonte, texto='Clique Aqui', cor_texto = PRETO)

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
        self.game.tela.fill(PRETO)
        self.botao.desenhar(self.game.tela)
        
