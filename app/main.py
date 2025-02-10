import pygame
from game import Game

pygame.init()
pygame.mixer.init()

game = Game()

game.executar()

pygame.quit()