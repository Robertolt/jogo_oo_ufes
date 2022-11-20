import sys
from typing import Tuple
import pygame as pg
# from bola import Bola

from config_jogo import ConfigJogo
from config_personagem import Personagem
from estado_jogo import EstadoJogo


class CenaPrincipal:
    def __init__(self, tela):
        self.tela = tela

        py = ConfigJogo.ALTURA_TELA // 2
        px_esq = ConfigJogo.LARGURA_TELA//2 - 10
        px_dir = ConfigJogo.LARGURA_TELA//2 + 10

        self.personagem1 = Personagem(posicao=(px_esq, py))
        self.personagem2 = Personagem(posicao=(px_dir, py))
        # self.bola = Bola()
        self.estado = EstadoJogo()

        self.encerrada = False

    def rodar(self):
        while not self.encerrada:
            self.tratamento_eventos()
            self.atualiza_estado()
            self.desenha()

    def tratamento_eventos(self):
        pg.event.get()

        # evento de saida
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)

        # personagem 1
        if pg.key.get_pressed()[pg.K_w]:
            self.personagem1.mover_para_cima()
        elif pg.key.get_pressed()[pg.K_s]:
            self.personagem1.mover_para_baixo()
        elif pg.key.get_pressed()[pg.K_a]:
            self.personagem1.mover_para_esquerda()
        elif pg.key.get_pressed()[pg.K_d]:
            self.personagem1.mover_para_direita()
        else:
            self.personagem1.parar()

        # personagem 2
        if pg.key.get_pressed()[pg.K_i]:
            self.personagem2.mover_para_cima()
        elif pg.key.get_pressed()[pg.K_k]:
            self.personagem2.mover_para_baixo()
        elif pg.key.get_pressed()[pg.K_j]:
            self.personagem2.mover_para_direita()
        elif pg.key.get_pressed()[pg.K_l]:
            self.personagem2.mover_para_esquerda()
        else:
            self.personagem2.parar()

    def atualiza_estado(self):
        self.personagem1.atualizar_posicao_x()
        self.personagem1.atualizar_posicao_y()
        self.personagem2.atualizar_posicao_x()
        self.personagem2.atualizar_posicao_y()
        #  self.bola.atualizar_posicao()

        if self.estado.jogo_terminou():
            self.encerrada = True

    def desenha(self):
        self.tela.fill((255, 255, 255))
        self.personagem1.desenha(self.tela)
        self.personagem2.desenha(self.tela)
        # self.bola.desenha(self.tela)
        self.estado.desenha(self.tela)
        pg.display.flip()
