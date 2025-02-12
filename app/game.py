import pygame
from config import LARGURA_TELA, ALTURA_TELA, FPS
from pages.menu import Menu
class Game:
    def __init__(self):
        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption("Meu Jogo")
        self.clock = pygame.time.Clock()
        self.executando = True
        self.fonte = pygame.font.SysFont("Arial", 50)

        self.volume_geral = 0.5
        
        self.musica_fundo = pygame.mixer.Sound("app/assets/musics/menu-musica.mp3")
        self.botao_hover_sound = pygame.mixer.Sound("app/assets/sounds/botao-hover-sound.mp3")
        
        self.pagina = Menu(self)
        
        self.cursor_imagem = pygame.image.load("app/assets/images/cursor.png")
        self.cursor_imagem = pygame.transform.scale(self.cursor_imagem, (32, 32))
        pygame.mouse.set_visible(False) 

        self.imagem_fundo = pygame.image.load('app/assets/images/gradiente_verde_azul.png')
        self.imagem_fundo = pygame.transform.scale(self.imagem_fundo, (LARGURA_TELA, ALTURA_TELA))
        
        self.musica_fundo.play(-1)
        self.musica_fundo.set_volume(self.volume_geral)

    def executar(self):
        while self.executando:
            self.pagina.capturar_eventos()
            self.pagina.atualizar()
            self.pagina.desenhar()
            pygame.display.flip()
            self.clock.tick(FPS)
            self.tela.blit(self.imagem_fundo,(0,0))


    def mudar_tela(self, nova_pagina):
        self.pagina = nova_pagina

    def desenhar_mouse(self):
        x, y = pygame.mouse.get_pos()
        self.tela.blit(self.cursor_imagem, (x, y))
        
    def alterar_volume_geral(self, volume):
        self.musica_fundo.set_volume(volume)
        self.botao_hover_sound.set_volume(volume)
        