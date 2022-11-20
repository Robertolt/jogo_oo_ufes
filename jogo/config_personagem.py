from typing import Tuple
import pygame
from config_jogo import ConfigJogo


class Personagem:
    VIDA = 20
    DANO = 2
    VELOCIDADE = 0.2

    # TIPO_ATAQUE = ATAQUE

    def __init__(self, posicao):
        self.posicao = posicao
        self.velocidade_y = 0
        self.velocidade_x = 0

    def mover_para_cima(self):
        self.velocidade_y = -ConfigJogo.VELOCIDADE_PERSONAGEM_Y

    def mover_para_baixo(self):
        self.velocidade_y = ConfigJogo.VELOCIDADE_PERSONAGEM_Y

    def mover_para_esquerda(self):
        self.velocidade_x = ConfigJogo.VELOCIDADE_PERSONAGEM_X

    def mover_para_direita(self):
        self.velocidade_x = - ConfigJogo.VELOCIDADE_PERSONAGEM_X

    def parar(self):
        self.velocidade_y = 0
        self.velocidade_x = 0

    def atualizar_posicao_y(self):
        x, y = self.posicao
        novo_y = y + self.velocidade_y

        if (novo_y >= 0) and \
                ((novo_y + ConfigJogo.ALTURA_PERSONAGEM) <= ConfigJogo.ALTURA_TELA):
            self.posicao = (x, novo_y)

    def atualizar_posicao_x(self):
        x, y = self.posicao
        novo_x = x + self.velocidade_x
        if (novo_x >= 0) and \
                ((novo_x + ConfigJogo.LARGURA_PERSONAGEM) <= ConfigJogo.LARGURA_TELA):
            self.posicao = (novo_x, y)

    def desenha(self, tela):
        x = self.posicao[0]
        y = self.posicao[1]
        l = ConfigJogo.LARGURA_PERSONAGEM
        a = ConfigJogo.ALTURA_PERSONAGEM
        pygame.draw.rect(
            tela,
            ConfigJogo.COR_PERSONAGEM,
            pygame.rect.Rect(x, y, l, a)
        )

    def rect(self) -> Tuple[float, float, float, float]:
        """ retorna os dados da barra como os retangulos sao representados
            no pygame, i.e., como uma tupla do tipo (px, py, largura, altura).
        """
        return self.posicao + (ConfigJogo.LARGURA_PERSONAGEM, ConfigJogo.ALTURA_PERSONAGEM)

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
