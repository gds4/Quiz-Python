import pygame

class Botao:
    def __init__(self, x, y, largura, altura, cor_botao, fonte, texto, cor_texto):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.fonte = fonte
        self.texto = texto
        self.cor_texto = cor_texto
        self.cor_botao = cor_botao 
        self.texto_renderizado = self.fonte.render(self.texto, True, cor_texto)
        self.texto_rect = self.texto_renderizado.get_rect(center=(self.x + self.largura // 2, self.y + self.altura // 2))

    def desenhar(self, tela):
        
        pygame.draw.rect(tela, self.cor_botao, (self.x, self.y, self.largura, self.altura), border_radius=15)
        
        tela.blit(self.texto_renderizado, self.texto_rect)

    def verificar_click(self, posicao):
        if (self.x <= posicao[0] <= self.x + self.largura and
            self.y <= posicao[1] <= self.y + self.altura):
            print("Botão pressionado!")