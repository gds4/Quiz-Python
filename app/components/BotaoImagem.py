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

    def mouse_em_cima(self):
        x, y = pygame.mouse.get_pos()
        return self.rect.collidepoint((x,y))

    def atualizar(self):
        self.imagem_atual = self.imagem_hover if self.mouse_em_cima() else self.imagem

    def desenhar(self, tela):
        tela.blit(self.imagem_atual, self.rect)

    def verificar_click(self, posicao):
        return self.rect.collidepoint(posicao)
