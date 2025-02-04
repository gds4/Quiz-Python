import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from states.menu import Menu

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Meu Jogo")
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.SysFont("Arial", 50)
        self.state = Menu(self)

    def run(self):
        while self.running:
            self.state.handle_events()
            self.state.update()
            self.state.draw()
            pygame.display.flip()
            self.clock.tick(FPS)

    def change_state(self, new_state):
        self.state = new_state
