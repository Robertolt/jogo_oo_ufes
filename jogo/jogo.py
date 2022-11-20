# este arquivo será responsável por rodar a tela do jogo
import pygame
import sys
from config_jogo import ConfigJogo
from cena_inicial import CenaInicial
from cena_principal import CenaPrincipal


class Jogo:
    def __init__(self):
        # inicialização básica
        pygame.init()
        # tamanho da tela
        self.tela = pygame.display.set_mode((ConfigJogo.LARGURA_TELA,
                                             ConfigJogo.ALTURA_TELA))

    def rodar(self):

        # cria a cena inicial
        cena = CenaInicial(self.tela)
        # fica na cena ate o usuario pressionar enter
        cena.rodar()
        # enquanto a janela nao for fechada

        while True:
            # cria a cena principal do jogo
            cena_principal = CenaPrincipal(self.tela)
            # roda a cena ate' um dos jogadores ganhar ou
            # chegar ao fim do jogo
            cena_principal.rodar()

        # para cada evento recebido



