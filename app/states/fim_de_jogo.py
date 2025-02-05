import pygame
from components.Botao import Botao  # Botão para voltar ao menu
  # Para voltar ao menu ao finalizar o jogo
from config import BRANCO, PRETO, CINZA, VERMELHO, VERMELHO_CLARO, LARGURA_TELA, ALTURA_TELA

class FimDeJogo:
    def __init__(self, game, pontuacao_final):
        self.game = game
        self.pontuacao_final = pontuacao_final
        self.font_titulo = pygame.font.Font(None, 64)
        self.font_info = pygame.font.Font(None, 36)

        # Cria um botão para voltar ao menu
        self.botao_menu = Botao(
            x=self.game.tela.get_width() // 2 - 100,
            y=self.game.tela.get_height() - 150,
            largura=200,
            altura=50,
            cor_botao_original=CINZA,
            cor_botao_hover=VERMELHO_CLARO,
            fonte=self.font_info,
            texto="Voltar ao Menu",
            cor_texto=PRETO
        )

    def capturar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.executando = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.botao_menu.verificar_click(pygame.mouse.get_pos()):
                    from states.menu import Menu
                    self.game.mudar_tela(Menu(self.game))

    def atualizar(self):
        self.botao_menu.atualizar()

    def desenhar(self):
        self.game.tela.fill(BRANCO)
        titulo = self.font_titulo.render("Fim de Jogo", True, PRETO)
        titulo_rect = titulo.get_rect(center=(self.game.tela.get_width() // 2, 100))
        self.game.tela.blit(titulo, titulo_rect)

        info = self.font_info.render(f"Sua pontuação: {self.pontuacao_final}", True, PRETO)
        info_rect = info.get_rect(center=(self.game.tela.get_width() // 2, 200))
        self.game.tela.blit(info, info_rect)

        self.botao_menu.desenhar(self.game.tela)
        self.game.desenhar_mouse()
