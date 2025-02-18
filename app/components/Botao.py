import pygame

class Botao:
    def __init__(self, x, y, largura, altura, cor_botao_original, cor_botao_hover, fonte, texto, cor_texto, som_hover):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

        self.cor_botao_original = cor_botao_original
        self.cor_botao_hover = cor_botao_hover
        self.cor_atual = cor_botao_original

        self.som_hover = som_hover
        self.emitir_som = False

        self.fonte = fonte
        self.texto = texto
        self.cor_texto = cor_texto
        self.tamanho_original = fonte.get_height()
        self.tamanho_atual = self.tamanho_original

        self.texto_renderizado = self.fonte.render(self.texto, True, cor_texto)
        self.texto_rect = self.texto_renderizado.get_rect(center=(self.x + self.largura // 2, self.y + self.altura // 2))

    def desenhar(self, tela):

        sombra_offset = 4
        sombra_rect = self.rect.move(sombra_offset, sombra_offset)
        pygame.draw.rect(tela, (50, 50, 50), sombra_rect, border_radius=15)

        pygame.draw.rect(tela, self.cor_atual, self.rect, border_radius=15)
        pygame.draw.rect(tela, (0, 0, 0), self.rect, width=3, border_radius=15)

        fonte_temp = pygame.font.Font(None, self.tamanho_atual)
        texto_renderizado = fonte_temp.render(self.texto, True, self.cor_texto)
        texto_rect = texto_renderizado.get_rect(center=self.rect.center)

        tela.blit(texto_renderizado, texto_rect)

    def atualizar(self):
        if self.verificar_colisao():
            self.cor_atual = self.cor_botao_hover
            self.tamanho_atual = int(self.tamanho_original * 1.1) 
            
            if not self.emitir_som:
                self.som_hover.play()
                self.emitir_som = True
        else:
            self.cor_atual = self.cor_botao_original
            self.tamanho_atual = self.tamanho_original  
            self.emitir_som = False

    def verificar_colisao(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
