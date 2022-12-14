import sys
from random import random, randint
from typing import Tuple
import pygame as pg

from config_jogo import ConfigJogo
from config_personagem import Personagem
from estado_jogo import EstadoJogo
from minions import Minions
from vetor import Vetor


class CenaPrincipal:
    def __init__(self, tela):
        self.tela = tela

        py = ConfigJogo.ALTURA_TELA // 2
        px_esq = ConfigJogo.LARGURA_TELA // 2 - 20
        px_dir = ConfigJogo.LARGURA_TELA // 2 + 20

        self.personagem1 = Personagem(posicao=(px_esq, py))
        self.personagem2 = Personagem(posicao=(px_dir, py))
        # self.bola = Bola()
        self.minions = Minions(posicao=(randint(0, ConfigJogo.LARGURA_TELA),
                                        randint(0, ConfigJogo.ALTURA_TELA)))
        self.minions1 = Minions(posicao=(randint(0, ConfigJogo.LARGURA_TELA),
                                         randint(0, ConfigJogo.ALTURA_TELA)))
        self.minions2 = Minions(posicao=(randint(0, ConfigJogo.LARGURA_TELA),
                                         randint(0, ConfigJogo.ALTURA_TELA)))
        self.minions3 = Minions(posicao=(randint(0, ConfigJogo.LARGURA_TELA),
                                         randint(0, ConfigJogo.ALTURA_TELA)))
        self.minions4 = Minions(posicao=(randint(0, ConfigJogo.LARGURA_TELA),
                                         randint(0, ConfigJogo.ALTURA_TELA)))
        self.estado = EstadoJogo()
        self.encerrada = False

        # Vetores pro minion
        self.vetor1 = Vetor(self.personagem1, self.minions)
        self.vetor2 = Vetor(self.personagem2, self.minions)

        # Vetores pro minion1
        self.vetor3 = Vetor(self.personagem1, self.minions1)
        self.vetor4 = Vetor(self.personagem2, self.minions1)

        # Vetores pro minion2
        self.vetor5 = Vetor(self.personagem1, self.minions2)
        self.vetor6 = Vetor(self.personagem2, self.minions2)

        # Vetores pro minion3
        self.vetor7 = Vetor(self.personagem1, self.minions3)
        self.vetor8 = Vetor(self.personagem2, self.minions3)

        # Vetores pro minion2
        self.vetor9 = Vetor(self.personagem1, self.minions4)
        self.vetor10 = Vetor(self.personagem2, self.minions4)

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
            self.personagem1.mover_para_direita()
        elif pg.key.get_pressed()[pg.K_d]:
            self.personagem1.mover_para_esquerda()
        else:
            self.personagem1.parar()

        # executar ataque personagem 1
        if pg.key.get_pressed()[pg.K_q]:
            self.personagem1.executar_ataque()

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

        # executar ataque personagem 2
        if pg.key.get_pressed()[pg.K_q]:
            self.personagem2.executar_ataque()

        # seguir para minion
        if self.vetor1.calcular() < self.vetor2.calcular():
            self.minions.mover_para(self.personagem1)
        else:
            self.minions.mover_para(self.personagem2)

        # seguir para minion1
        if self.vetor3.calcular() < self.vetor4.calcular():
            self.minions1.mover_para(self.personagem1)
        else:
            self.minions1.mover_para(self.personagem2)

        # seguir para minion2
        if self.vetor5.calcular() < self.vetor6.calcular():
            self.minions2.mover_para(self.personagem1)
        else:
            self.minions2.mover_para(self.personagem2)

        # seguir para minion3
        if self.vetor7.calcular() < self.vetor8.calcular():
            self.minions3.mover_para(self.personagem1)
        else:
            self.minions3.mover_para(self.personagem2)

        # seguir para minion3
        if self.vetor9.calcular() < self.vetor10.calcular():
            self.minions4.mover_para(self.personagem1)
        else:
            self.minions4.mover_para(self.personagem2)

    def atualiza_estado(self):
        self.personagem1.atualizar_posicao_x()
        self.personagem1.atualizar_posicao_y()

        self.personagem2.atualizar_posicao_x()
        self.personagem2.atualizar_posicao_y()

        if self.estado.jogo_terminou():
            self.encerrada = True

    def desenha(self):
        self.tela.fill((255, 255, 255))
        self.personagem1.desenha(self.tela)
        self.personagem2.desenha(self.tela)
        self.minions.desenha(self.tela)
        self.minions1.desenha(self.tela)
        self.minions2.desenha(self.tela)
        self.minions3.desenha(self.tela)
        self.minions4.desenha(self.tela)
        self.estado.desenha(self.tela)

        # desenha ataque personagem 1
        if pg.key.get_pressed()[pg.K_q]:
            self.personagem1.desenha_ataque(self.tela)

        # desenha ataque personagem 2
        if pg.key.get_pressed()[pg.K_u]:
            self.personagem2.desenha_ataque(self.tela)

        pg.display.flip()
