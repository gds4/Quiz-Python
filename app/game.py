import pygame
from config import LARGURA_TELA, ALTURA_TELA, FPS
from states.Menu import Menu

class Game:
    def __init__(self):
        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption("Meu Jogo")
        self.clock = pygame.time.Clock()
        self.executando = True
        self.fonte = pygame.font.SysFont("Arial", 50)
        self.pagina = Menu(self)

    def executar(self):
        while self.executando:
            self.pagina.capturar_eventos()
            self.pagina.atualizar()
            self.pagina.desenhar()
            pygame.display.flip()
            self.clock.tick(FPS)

    def mudar_tela(self, nova_pagina):
        self.pagina = nova_pagina
