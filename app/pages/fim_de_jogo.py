import pygame
from components.Botao import Botao
from components.BotaoImagem import BotaoImagem
from config import  PRETO, CINZA, VERMELHO_CLARO

class FimDeJogo:
    def __init__(self, game, pontuacao_final):
        self.game = game
        self.pontuacao_final = pontuacao_final
        self.font_titulo = pygame.font.Font(None, 64)
        self.font_info = pygame.font.Font(None, 32)

        self.botao_reiniciar = Botao(
            x=self.game.tela.get_width() // 2 - 100,
            y=self.game.tela.get_height() - 200,
            largura=200,
            altura=50,
            cor_botao_original=CINZA,
            cor_botao_hover=VERMELHO_CLARO,
            fonte=self.font_info,
            texto="Jogar novamente",
            cor_texto=PRETO,
            som_hover= self.game.botao_hover_sound
        )
        self.botao_menu = BotaoImagem(
            x = (self.game.tela.get_width() // 2 ) - 15,
            y = 550,
            altura = 40,
            largura = 40,
            caminho_imagem = 'app/assets/images/menu.png',
            caminho_imagem_hover = 'app/assets/images/menu_hover.png',
        )

    def capturar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.executando = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.botao_reiniciar.verificar_colisao():
                    from pages.jogo import Jogo
                    self.game.mudar_tela(Jogo(self.game))
                if self.botao_menu.verificar_colisao():
                    from pages.menu import Menu
                    self.game.mudar_tela(Menu(self.game))

    def atualizar(self):
        self.botao_menu.atualizar()
        self.botao_reiniciar.atualizar()

    def desenhar(self):
                
        titulo = self.font_titulo.render("Fim de Jogo", True, PRETO)
        titulo_rect = titulo.get_rect(center=(self.game.tela.get_width() // 2, 100))
        self.game.tela.blit(titulo, titulo_rect)

        info = self.font_info.render(f"Sua pontuação: {self.pontuacao_final}", True, PRETO)
        info_rect = info.get_rect(center=(self.game.tela.get_width() // 2, 200))
        self.game.tela.blit(info, info_rect)

        self.botao_menu.desenhar(self.game.tela)
        self.botao_reiniciar.desenhar(self.game.tela)
        self.game.desenhar_mouse()
