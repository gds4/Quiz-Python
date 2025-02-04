import pygame

class Botao:
    def __init__(self, x, y, largura, altura, cor_botao_original, cor_botao_hover, fonte, texto, cor_texto):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

        self.cor_botao_original = cor_botao_original 
        self.cor_botao_hover = cor_botao_hover
        self.cor_atual = cor_botao_original

        self.fonte = fonte
        self.texto = texto
        self.cor_texto = cor_texto
        self.texto_renderizado = self.fonte.render(self.texto, True, cor_texto)
        self.texto_rect = self.texto_renderizado.get_rect(center=(self.x + self.largura // 2, self.y + self.altura // 2))

    def desenhar(self, tela):
        
        pygame.draw.rect(tela, self.cor_atual, (self.x, self.y, self.largura, self.altura), border_radius=15)
        
        tela.blit(self.texto_renderizado, self.texto_rect)

    def mouse_em_cima(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return self.x <= mouse_x <= self.x + self.largura and self.y <= mouse_y <= self.y + self.altura

    def atualizar(self):
        if self.mouse_em_cima():
            self.cor_atual = self.cor_botao_hover
        else:
            self.cor_atual = self.cor_botao_original


    def verificar_click(self, posicao):
        if (self.x <= posicao[0] <= self.x + self.largura and
            self.y <= posicao[1] <= self.y + self.altura):
            return True