import pygame
import sys
from components.Botao import Botao 
from config import BRANCO, PRETO, CINZA, VERMELHO, VERMELHO_CLARO, LARGURA_TELA, ALTURA_TELA
from states.jogo import Jogo
from states.jogo_multiplayer import JogoMultiplayer

class Menu:
    def __init__(self, game):
        self.game = game  # Referência ao jogo principal
        self.fonte = pygame.font.Font(None, 48)
        self.botaoJogar = Botao(
            x=80, 
            y=380, 
            largura=200, 
            altura=50, 
            cor_botao_original = BRANCO, 
            cor_botao_hover = CINZA, 
            fonte=self.fonte, 
            texto='Jogar', 
            cor_texto = PRETO
        )
        
        self.botaoMultiplayer = Botao(
            x=80, 
            y=450, 
            largura=200, 
            altura=50, 
            cor_botao_original = BRANCO, 
            cor_botao_hover = CINZA, 
            fonte=self.fonte, 
            texto='multiplayer', 
            cor_texto = PRETO
        )

        self.botaoSair = Botao(
            x=80, 
            y=520, 
            largura=200, 
            altura=50, 
            cor_botao_original = VERMELHO,
            cor_botao_hover = VERMELHO_CLARO, 
            fonte=self.fonte, 
            texto='Sair', 
            cor_texto = PRETO
        )
        self.imagem_fundo = pygame.image.load('app/assets/gradiente_verde_azul.png')
        self.imagem_fundo = pygame.transform.scale(self.imagem_fundo, (LARGURA_TELA, ALTURA_TELA))
        self.quiz_image = pygame.image.load('app/assets/quiz.png')
        self.quiz_image = pygame.transform.scale(self.quiz_image, (300, 300))


    def capturar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.executando = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.botaoSair.verificar_colisao():
                    self.game.executando = False
                if self.botaoJogar.verificar_colisao():
                    self.game.mudar_tela(Jogo(self.game))
                if self.botaoMultiplayer.verificar_colisao():
                    self.game.mudar_tela(JogoMultiplayer(self.game))
                    
    def atualizar(self):
        self.botaoJogar.atualizar()
        self.botaoMultiplayer.atualizar()
        self.botaoSair.atualizar()
        pass

    def desenhar(self):
        #Desenha o menu na tela
        self.game.tela.blit(self.imagem_fundo,(0,0))
        self.game.tela.blit(self.quiz_image, (30,50))
        self.botaoJogar.desenhar(self.game.tela)
        self.botaoMultiplayer.desenhar(self.game.tela)
        self.botaoSair.desenhar(self.game.tela)
        self.game.desenhar_mouse()

        
