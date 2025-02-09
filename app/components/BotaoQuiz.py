import pygame
from config import NEUTRA, CINZA, VERDE, VERMELHO

class BotaoQuiz:
    def __init__(self, x, y, largura, altura, fonte, texto, cor_texto, resposta,
                 cor_neutra=NEUTRA, cor_hover=CINZA, cor_correto=VERDE, cor_errado=VERMELHO):
      
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

        self.fonte = fonte
        self.texto = texto
        self.cor_texto = cor_texto
        self.resposta = resposta  # Objeto Resposta, possui atributo 'correta' (boolean)

        self.cor_neutra = cor_neutra
        self.cor_hover = cor_hover
        self.cor_correto = cor_correto
        self.cor_errado = cor_errado

        self.cor_atual = cor_neutra
        self.locked = False  # Bloqueia alterações depois de selecionado

        self.texto_renderizado = self.fonte.render(self.texto, True, self.cor_texto)
        self.texto_rect = self.texto_renderizado.get_rect(
            center=(self.x + self.largura // 2, self.y + self.altura // 2)
        )

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor_atual, (self.x, self.y, self.largura, self.altura), border_radius=8)
        tela.blit(self.texto_renderizado, self.texto_rect)

    def mouse_em_cima(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return (self.x <= mouse_x <= self.x + self.largura and
                self.y <= mouse_y <= self.y + self.altura)

    def atualizar(self):
        if not self.locked:
            if self.mouse_em_cima():
                self.cor_atual = self.cor_hover
            else:
                self.cor_atual = self.cor_neutra

    def verificar_click(self, posicao):
        return (self.x <= posicao[0] <= self.x + self.largura and
                self.y <= posicao[1] <= self.y + self.altura)

    def marcar_resposta(self):
        self.locked = True
        if hasattr(self.resposta, 'correta'):
            if self.resposta.correta:
                self.cor_atual = self.cor_correto
                return True
            else:
                self.cor_atual = self.cor_errado
                return False
        else:
            if self.resposta["correta"]:
                self.cor_atual = self.cor_correto
                return True
            else:
                self.cor_atual = self.cor_errado
                return False