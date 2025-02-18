import pygame
from config import AZUL_CLARO, BRANCO, CINZA, VERDE, VERMELHO, CINZA_ESCURO

class BotaoQuiz:
    def __init__(self, x, y, largura, altura, fonte, texto, cor_texto, resposta,
                 cor_neutra=AZUL_CLARO, cor_hover=CINZA, cor_correto=VERDE, cor_errado=VERMELHO):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.sombra_rect = pygame.Rect(x + 3, y + 3, largura, altura)
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

        self.fonte = fonte
        self.texto = texto
        self.cor_texto = cor_texto
        self.resposta = resposta  

        self.cor_neutra = cor_neutra
        self.cor_hover = cor_hover
        self.cor_correto = cor_correto
        self.cor_errado = cor_errado

        self.cor_atual = cor_neutra
        self.locked = False 

        self.texto_renderizado = self.fonte.render(self.texto, True, self.cor_texto)
        self.texto_rect = self.texto_renderizado.get_rect(
            center=(self.x + self.largura // 2, self.y + self.altura // 2)
        )

    def desenhar(self, tela):
        pygame.draw.rect(tela, CINZA_ESCURO, self.sombra_rect, border_radius=15) 
        pygame.draw.rect(tela, self.cor_atual, self.rect, border_radius=15)
        pygame.draw.rect(tela, BRANCO, self.rect, width=2, border_radius=15)
        tela.blit(self.texto_renderizado, self.texto_rect)

    def atualizar(self):
        if not self.locked:
            if self.verificar_colisao():
                self.cor_atual = self.cor_hover
            else:
                self.cor_atual = self.cor_neutra

    def verificar_colisao(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
    
    def marcar_resposta(self):
        self.locked = True
       
        if self.resposta["correta"]:
            self.cor_atual = self.cor_correto
            return True
        else:
            self.cor_atual = self.cor_errado
            return False
