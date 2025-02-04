import pygame
import sys
from config import WHITE, BLACK

class Menu:
    def __init__(self, game):
        self.game = game  # Referência ao jogo principal
        self.font = pygame.font.Font(None, 48)  # Fonte do menu
        self.options = ["Jogar", "Sair"]
        self.selected = 0  # Opção selecionada

    def handle_events(self):
        """Captura eventos do teclado."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                pygame.quit()
                sys.exit()
    def update(self):
        """Atualiza a lógica do menu (se necessário)."""
        pass

    def draw(self):
        #Desenha o menu na tela
        self.game.screen.fill(BLACK)
        
