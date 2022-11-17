# este arquivo será responsável por rodar a tela do jogo
import pygame
import sys
from config_jogo import ConfigJogo
from cena_inicial import CenaInicial


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
            self.tratamento_de_eventos()
            # self.atualiza_estado()
            self.desenha_na_tela()

        # para cada evento recebido

    def tratamento_de_eventos(self):
        pygame.event.get()

        # se for recebido o evento de fechar a janela (ex.: usuario clicou no 'x') ...
        # evento de saída
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            print("Encerrando o programa.")
            sys.exit(0)

    def desenha_na_tela(self):
        # preenche a tela com branco
        self.tela.fill((255, 255, 255))
        # atualiza a tela
        pygame.display.flip()


def main():
    Jogo().rodar()


if __name__ == '__main__':
    main()
