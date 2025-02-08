import pygame

class BarraExperiencia:
    def __init__(self, x, y, largura=300, altura=20, usuario=None, nivel=None, xp=None):
        """
        Parâmetros:
          - x, y: posição na tela onde a barra será desenhada.
          - largura, altura: dimensões da barra.
          - usuario: objeto do tipo Usuario. Se fornecido, extrai nivel e xp_atual.
          - nivel e xp: caso não seja passado um usuário, é possível fornecer esses valores diretamente.
        """
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.xp_por_nivel = 20000  # Cada nível equivale a 20000 xp

        if usuario is not None:
            self.nivel = usuario.nivel
            self.xp = usuario.xp_atual
        else:
            self.nivel = nivel if nivel is not None else 1
            self.xp = xp if xp is not None else 0

        self._atualizar_progress()
        self.animando = False

    def _atualizar_progress(self):
        """
        Atualiza a fração de preenchimento da barra.
        """
        # xp no nível atual (caso ultrapasse 20000, é considerado que houve level up)
        xp_no_nivel = self.xp % self.xp_por_nivel
        self.progress = xp_no_nivel / self.xp_por_nivel

    def desenhar(self, tela):
        """
        Desenha a barra de experiência na superfície 'tela'.
        """
        # Desenha o fundo da barra (cor cinza)
        cor_fundo = (50, 50, 50)
        pygame.draw.rect(tela, cor_fundo, (self.x, self.y, self.largura, self.altura))
        
        # Desenha a parte preenchida (cor verde)
        fill_width = int(self.progress * self.largura)
        cor_preenchimento = (0, 255, 0)
        pygame.draw.rect(tela, cor_preenchimento, (self.x, self.y, fill_width, self.altura))
        
        # Desenha a borda da barra
        cor_borda = (255, 255, 255)
        pygame.draw.rect(tela, cor_borda, (self.x, self.y, self.largura, self.altura), 2)
        
        # Exibe o nível do usuário sobre a barra (opcional)
        fonte = pygame.font.Font(None, 24)
        texto = fonte.render(f"Nível {self.nivel}", True, (255, 255, 255))
        tela.blit(texto, (self.x + self.largura + 10, self.y - 5))

    def animar_evolucao(self, xp_adicional, tela):
        """
        Anima a evolução da barra adicionando gradualmente o xp_adicional.
        Se o xp ultrapassar o limite para level up, incrementa o nível e continua a animação.
        
        Parâmetros:
          - xp_adicional: quantidade de xp a ser adicionada.
          - tela: a superfície onde a animação será desenhada.
        """
        self.animando = True
        xp_inicial = self.xp
        xp_target = self.xp + xp_adicional
        
        # Configura um clock para controlar os frames da animação.
        clock = pygame.time.Clock()
        
        # Define o incremento por frame (supondo 60 frames para a animação)
        incremento = xp_adicional / 60.0
        
        while self.xp < xp_target:
            self.xp += incremento
            if self.xp > xp_target:
                self.xp = xp_target
            
            # Verifica se houve level up (xp ultrapassou o limite do nível)
            while self.xp >= self.xp_por_nivel:
                self.nivel += 1
                self.xp -= self.xp_por_nivel
            
            self._atualizar_progress()
            
            # Atualiza a tela: normalmente, você deve limpar a tela e redesenhar todos os componentes.
            # Aqui, para simplicidade, assumimos que apenas a barra é desenhada.
            tela.fill((0, 0, 0))  # Limpa a tela com fundo preto
            self.desenhar(tela)
            pygame.display.flip()
            clock.tick(60)  # 60 frames por segundo
        
        self.animando = False
