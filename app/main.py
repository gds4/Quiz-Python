import pygame
from game import Game

print('\nexecutando pygame')
pygame.init()

print('\ninicializando game')
game = Game()

print('\nexecutando game')
game.executar()
print('\n finalizando app quiz')
pygame.quit()