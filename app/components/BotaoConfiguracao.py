import pygame
from components.BotaoImagem import BotaoImagem

class BotaoConfiguracao:
    def __init__(self, x, y, game):
        self.game = game  # Referência para acessar self.game.musica_fundo
        self.x = x
        self.y = y
        self.largura = 40
        self.altura = 40

        self.imagem = pygame.transform.scale(
            pygame.image.load('app/assets/images/reiniciar.png'),
            (self.largura, self.altura)
        )
        self.imagem_hover = pygame.transform.scale(
            pygame.image.load('app/assets/images/reiniciar_hover.png'),
            (self.largura, self.altura)
        )
        self.rect = self.imagem.get_rect(topleft=(x, y))

        # Estado para animação e exibição dos botões de volume
        self.animando = False
        self.progresso_animacao = 0  # Valor de 0 a 1 que indica o progresso da animação
        self.abrindo = True          # True para abertura (exibir botões) ou False para fechamento
        self.mostrar_botoes = False  # Flag que indica se os botões de volume estão abertos

        self.volume = 5  # Volume inicial (escala de 0 a 10)

        # Cria os botões de volume usando a classe BotaoImagem.
        # Eles iniciam exatamente na posição do botão de configuração (ou seja, "atrás dele")
        self.botao_volume_up = BotaoImagem(
            x, y, 40, 40,
            'app/assets/images/volume-up.png',
            'app/assets/images/volume-up.png'
        )
        self.botao_volume_down = BotaoImagem(
            x, y, 40, 40,
            'app/assets/images/volume-down.png',
            'app/assets/images/volume-down.png'
        )

        # Posições finais desejadas para os botões de volume (ambos deslizam para a esquerda)
        self.pos_final_volume_up_x = self.x - 50
        self.pos_final_volume_down_x = self.x - 100

    def atualizar(self):
        """
        Atualiza a animação de deslize dos botões de volume.
        """
        if self.animando:
            # Incrementa o progresso da animação (ajuste a velocidade conforme necessário)
            self.progresso_animacao += 0.05
            progress = min(self.progresso_animacao, 1.0)
            
            if self.abrindo:
                # Interpolação: do x original para a posição final à esquerda
                novo_x_up = self.x + (self.pos_final_volume_up_x - self.x) * progress
                novo_x_down = self.x + (self.pos_final_volume_down_x - self.x) * progress
            else:
                # Fechando: da posição final de volta para a posição do botão de configuração
                novo_x_up = self.pos_final_volume_up_x + (self.x - self.pos_final_volume_up_x) * progress
                novo_x_down = self.pos_final_volume_down_x + (self.x - self.pos_final_volume_down_x) * progress

            self.botao_volume_up.rect.x = int(novo_x_up)
            self.botao_volume_down.rect.x = int(novo_x_down)
            self.botao_volume_up.rect.y = self.y
            self.botao_volume_down.rect.y = self.y

            if progress >= 1.0:
                self.animando = False
                self.progresso_animacao = 0
                if self.abrindo:
                    self.mostrar_botoes = True
                    # Garante que os botões estejam exatamente na posição final
                    self.botao_volume_up.rect.x = self.pos_final_volume_up_x
                    self.botao_volume_down.rect.x = self.pos_final_volume_down_x
                else:
                    self.mostrar_botoes = False
                    # Retorna os botões para a posição do botão de configuração
                    self.botao_volume_up.rect.x = self.x
                    self.botao_volume_down.rect.x = self.x

        # Atualiza o estado (ex.: hover) dos botões de volume
        self.botao_volume_up.atualizar()
        self.botao_volume_down.atualizar()

    def desenhar(self, tela):
        """
        Desenha os botões de volume (atrás) e, por cima deles, o botão de configuração.
        """
        # Primeiro desenha os botões de volume (se estiverem abertos ou durante a animação)
        if self.mostrar_botoes or self.animando:
            self.botao_volume_up.desenhar(tela)
            self.botao_volume_down.desenhar(tela)

        # Seleciona a imagem do botão de configuração de acordo com o estado:
        # Se os botões de volume estiverem abertos ou se estiver animando para abrir, usa a imagem hover.
        if self.mostrar_botoes or (self.animando and self.abrindo):
            imagem_botao = self.imagem_hover
        else:
            imagem_botao = self.imagem

        tela.blit(imagem_botao, self.rect)

    def clicar(self):
        """
        Processa o clique do mouse.
          - Se os botões de volume estiverem abertos, verifica primeiro se o clique ocorreu sobre eles.
          - Caso contrário, se o clique ocorreu sobre o botão de configuração (área principal),
            inicia a animação de abertura/fechamento.
        """
        mouse_pos = pygame.mouse.get_pos()
        if not self.animando:
            # Se os botões de volume estão abertos, testa se o clique foi neles.
            if self.mostrar_botoes:
                if self.botao_volume_up.verificar_colisao():
                    self.volume = min(self.volume + 1, 10)
                    print("Volume UP:", self.volume)
                    self.game.alterar_volume_geral(self.volume / 10.0)
                    return  # Evita que o clique também acione o botão principal
                elif self.botao_volume_down.verificar_colisao():
                    self.volume = max(self.volume - 1, 0)
                    print("Volume DOWN:", self.volume)
                    self.game.alterar_volume_geral(self.volume / 10.0)
                    return
            # Se o clique não for sobre os botões de volume, verifica se foi sobre o botão de configuração.
            if self.rect.collidepoint(mouse_pos):
                # Inverte o estado: se estiver aberto, inicia o fechamento; se estiver fechado, inicia a abertura
                self.abrindo = not self.mostrar_botoes
                self.animando = True
                self.progresso_animacao = 0

    def verificar_colisao(self):
        """ Verifica se o mouse está sobre o botão de configuração (área principal). """
        return self.rect.collidepoint(pygame.mouse.get_pos())
