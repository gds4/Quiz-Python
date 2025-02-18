import pygame
import sys
from components.Botao import Botao 
from components.BotaoConfiguracao import BotaoConfiguracao
from config import BRANCO, PRETO, CINZA, VERMELHO, VERMELHO_CLARO, LARGURA_TELA, ALTURA_TELA
from pages.jogo import Jogo
from pages.jogo_multiplayer import JogoMultiplayer

class Menu:
    def __init__(self, game):
        self.game = game  
        self.fonte = pygame.font.Font(None, 48)
        
        self.botao_jogar = Botao(
            x=80, 
            y=380, 
            largura=200, 
            altura=50, 
            cor_botao_original=BRANCO, 
            cor_botao_hover=CINZA, 
            fonte=self.fonte, 
            texto='Jogar', 
            cor_texto=PRETO,
            som_hover= self.game.botao_hover_sound
        )
        
        self.botao_multiplayer = Botao(
            x=80, 
            y=450, 
            largura=200, 
            altura=50, 
            cor_botao_original=BRANCO, 
            cor_botao_hover=CINZA, 
            fonte=self.fonte, 
            texto='Multiplayer', 
            cor_texto=PRETO,
            som_hover= self.game.botao_hover_sound
        )

        self.botaoSair = Botao(
            x=80, 
            y=520, 
            largura=200, 
            altura=50, 
            cor_botao_original=VERMELHO,
            cor_botao_hover=VERMELHO_CLARO, 
            fonte=self.fonte, 
            texto='Sair', 
            cor_texto=PRETO,
            som_hover= self.game.botao_hover_sound
        )
        
        self.botao_configuracao = BotaoConfiguracao(
            x=310, 
            y=10, 
            game=self.game
        )

        self.imagem_fundo = pygame.image.load('app/assets/images/gradiente_verde_azul.png')
        self.imagem_fundo = pygame.transform.scale(self.imagem_fundo, (LARGURA_TELA, ALTURA_TELA))
        self.quiz_image = pygame.image.load('app/assets/images/quiz.png')
        self.quiz_image = pygame.transform.scale(self.quiz_image, (300, 300))

    def capturar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.executando = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.botao_configuracao.clicar()
                if self.botaoSair.verificar_colisao():
                    self.game.executando = False
                if self.botao_jogar.verificar_colisao():
                    self.game.mudar_tela(Jogo(self.game))
                if self.botao_multiplayer.verificar_colisao():
                    self.game.mudar_tela(JogoMultiplayer(self.game))


    def atualizar(self):
        self.botao_jogar.atualizar()
        self.botao_multiplayer.atualizar()
        self.botaoSair.atualizar()
        self.botao_configuracao.atualizar() 

    def desenhar(self):
        self.game.tela.blit(self.imagem_fundo, (0, 0))
        self.game.tela.blit(self.quiz_image, (30, 50))
        self.botao_jogar.desenhar(self.game.tela)
        self.botao_multiplayer.desenhar(self.game.tela)
        self.botaoSair.desenhar(self.game.tela)
        self.botao_configuracao.desenhar(self.game.tela) 
        self.game.desenhar_mouse()
