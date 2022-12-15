import pygame
from config_personagem import Personagem
from config_jogo import ConfigJogo


class Minions:
    def __init__(self, posicao):
        self.dano = ConfigJogo.DANO_MINIONS
        self.vida = ConfigJogo.VIDA_MINIONS
        self.posicao = posicao
        self.velocidade_y = ConfigJogo.VELOCIDADE_MINIONS_Y
        self.velocidade_x = ConfigJogo.VELOCIDADE_MINIONS_X

    def mover_para(self, p):
        xp, yp = p.posicao
        xm, ym = self.posicao
        if xp > xm:
            xm += self.velocidade_x
            self.posicao = (xm, ym)
        else:
            xm -= self.velocidade_x
            self.posicao = (xm, ym)

        if yp > ym:
            ym += self.velocidade_y
            self.posicao = (xm, ym)
        else:
            ym -= self.velocidade_y
            self.posicao = (xm, ym)

    # def seguir_personagem_x(self):
    #     xp, yp = super().mostrar_a_posicao()  # coordenadas personagens
    #     xm, ym = self.posicao  # coordenadas minions
    #     novo_xm = xm + self.velocidade_x
    #     if xp >= xm:
    #         while xm < xp:
    #             self.posicao = (novo_xm, ym)
    #     else:
    #         while xm > xp:
    #             novo_xm = xm - self.velocidade_x
    #             self.posicao = (novo_xm, ym)
    #
    # def seguir_personagem_y(self):
    #     xp, yp = super().mostrar_a_posicao()  # coordenadas personagens
    #     xm, ym = self.posicao  # coordenadas minions
    #     novo_ym = ym + self.velocidade_y
    #     if xp >= xm:
    #         while ym < yp:
    #             self.posicao = (xm, novo_ym)
    #     else:
    #         while ym > yp:
    #             novo_ym = ym - self.velocidade_y
    #             self.posicao = (xm, novo_ym)

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

    def encostou_no_personagem(self, p):
        xp, yp = p.posicao
        xm, ym = self.posicao
        if (xm < xp) and (xp < xm + 10) and (ym < yp) and (yp < ym + 10):
            return True


