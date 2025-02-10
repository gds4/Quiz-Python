import pygame

class BotaoImagem:
    def __init__(self, x, y, largura, altura, caminho_imagem, caminho_imagem_hover):

        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        
        self.imagem = pygame.image.load(caminho_imagem)
        self.imagem = pygame.transform.scale(self.imagem, (largura, altura))

        self.imagem_hover = pygame.image.load(caminho_imagem_hover)
        self.imagem_hover = pygame.transform.scale(self.imagem_hover, (largura, altura))

        self.imagem_atual = self.imagem

        self.rect = self.imagem.get_rect(topleft=(x, y))

    def atualizar(self):
        self.imagem_atual = self.imagem_hover if self.verificar_colisao() else self.imagem

    def desenhar(self, tela):
        tela.blit(self.imagem_atual, self.rect)

    def verificar_colisao(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
