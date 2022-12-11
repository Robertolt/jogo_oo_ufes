import pygame
from config_personagem import Personagem
from config_jogo import ConfigJogo


class Minions:
    def __init__(self, posicao):
        self.dano = ConfigJogo.DANO_MINIONS
        self.vida = ConfigJogo.VIDA_MINIONS
        self.posicao = posicao
        self.velocidade_y = 0
        self.velocidade_x = 0

    def seguir_personagens(self):
        pass

    def desenha(self, tela):
        x = self.posicao[0]
        y = self.posicao[1]
        l = ConfigJogo.LARGURA_MINION
        a = ConfigJogo.ALTURA_MINION
        pygame.draw.rect(
            tela,
            ConfigJogo.COR_PERSONAGEM,
            pygame.rect.Rect(x, y, l, a)
        )

    def rect(self):
        """ retorna os dados da barra como os retangulos sao representados
            no pygame, i.e., como uma tupla do tipo (px, py, largura, altura).
        """
        return self.posicao + (ConfigJogo.LARGURA_PERSONAGEM, ConfigJogo.ALTURA_PERSONAGEM)

    def qntde_minions(self):
        pass