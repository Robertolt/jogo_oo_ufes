from typing import Tuple
import pygame
from config_jogo import ConfigJogo


class Personagem:
    VIDA = 20
    DANO = 2
    VELOCIDADE = 0.2
    TIPO_ATAQUE = ATAQUE

        def __init__(self, posicao):
            self.posicao = posicao
            self.velocidade = 0

        def mover_para_cima(self):
            self.velocidade = -ConfigJogo.VELOCIDADE_PERSONAGEM

        def mover_para_baixo(self):
            self.velocidade = ConfigJogo.VELOCIDADE_PERSONAGEM

        def parar(self):
            self.velocidade = 0

        def atualizar_posicao(self):
            x, y = self.posicao
            novo_y = y + self.velocidade
            novo_x = x + self.velocidade

            if (novo_y >= 0) and \
                    ((novo_y + ConfigJogo.ALTURA_PERSONAGEM) <= ConfigJogo.ALTURA_TELA):
                self.posicao = (x, novo_y)

            if (novo_x >= 0) and \
                    ((novo_x + ConfigJogo.ALTURA_PERSONAGEM) <= ConfigJogo.LARGURA_TELA):
                self.posicao = (novo_x, y)

        def desenha(self, tela):
            x = self.posicao[0]
            y = self.posicao[1]
            l = ConfigJogo.LARGURA_BARRA
            a = ConfigJogo.ALTURA_BARRA
            pygame.draw.rect(
                tela,
                ConfigJogo.COR_BARRA,
                pygame.rect.Rect(x, y, l, a)
            )

        def rect(self) -> Tuple[float, float, float, float]:
            """ retorna os dados da barra como os retangulos sao representados
                no pygame, i.e., como uma tupla do tipo (px, py, largura, altura).
            """
            return self.posicao + (ConfigJogo.LARGURA_BARRA, ConfigJogo.ALTURA_BARRA)


# class Mago(Personagem):
#     def __init__(self, tipo_ataque):
#         self.tipo_ataque = magia  # bola de fogo ao redor
#
#
# class Lutador(Personagem):
#     def __init__(self):
#         self.DANO = Personagem.DANO * 2
#
#
# class Curandeiro(Personagem):
#     def __init__(self, curar):
#         self.curar = curar
#
#
# class Atirador(Personagem):
#     def __init__(self):
#         self.tiro = tiro