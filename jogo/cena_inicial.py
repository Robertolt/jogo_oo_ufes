import pygame
import sys
from config_jogo import ConfigJogo
from cronometro import Cronometro

""" nessa cena Deve ser criada uma tela de apresentação além da tela principal do jogo. Na tela de
 apresentação, deve ser escrita a história de background básica do jogo e nela os jogadores
 podem escolher os personagens que usarão na partida. O mesmo personagem pode ser
 escolhido pelos 2 jogadores"""


class CenaInicial:
    def __init__(self, tela):
        self.tela = tela
        self.encerrada = False

        # cria os textos que serao mostrados na tela
        font_titulo = pygame.font.SysFont(None, ConfigJogo.FONTE_TITULO)
        font_subtitulo = pygame.font.SysFont(None, ConfigJogo.FONTE_SUBTITULO)
        self.titulo = font_titulo.render(
            f'Planet Saver', True, ConfigJogo.COR_TITULO)
        self.subtitulo = font_subtitulo.render(
            f'Salve o planeta do lixo maldoso'
            f' enquanto ainda há tempo', True, ConfigJogo.COR_TITULO)
        self.subtitulo_2 = font_subtitulo.render(
            f'Devido a grande quantidade de lixo com destinação incorreta, houve o superaquecimento do planeta e, '
            f'também a '
            f'impossibilidade das correntes marítimas de continuarem a fluir. É seu dever destruir o lixo que sobrou '
            f'e salvar o planete ', True, ConfigJogo.COR_TITULO)

        # variaveis usadas para fazer o subtitulo piscar
        self.cronometro = Cronometro()
        self.mostrar_subtitulo = True

    def rodar(self):
        while not self.encerrada:
            self.tratamento_eventos()
            self.atualiza_estado()
            self.desenha()

    def tratamento_eventos(self):
        pygame.event.get()

        # evento de saida
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            sys.exit(0)

        # evento de prosseguimento
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.encerrada = True

    def atualiza_estado(self):
        if self.cronometro.tempo_passado() > 0.1:
            self.mostrar_subtitulo = not self.mostrar_subtitulo
            self.cronometro.reset()

    def desenha(self):
        self.tela.fill((255, 255, 255))
        # self.barra_direita.desenha(self.tela)
        # self.barra_esquerda.desenha(self.tela)
        # self.bola.desenha(self.tela)
        self.desenha_titulo(self.tela)
        self.desenha_subtitulo(self.tela)
        self.desenha_subtitulo_2(self.tela)
        pygame.display.flip()

    def desenha_titulo(self, tela):
        # desenha o titulo no meio da tela
        px = ConfigJogo.LARGURA_TELA // 2 - self.titulo.get_size()[0] // 2
        py = (0.2 * ConfigJogo.ALTURA_TELA // 2)
        tela.blit(self.titulo, (px, py))

    def desenha_subtitulo(self, tela):
        if self.mostrar_subtitulo:
            # desenha o subtitulo centralizado horizontalmente, mas verticalmente
            # abaixo do titulo. Ao somar "self.titulo.get_size()[1] * 1.5" no py,
            # estamos deslocando 1.5x a altura do titulo para baixo.
            px = ConfigJogo.LARGURA_TELA // 2 - \
                 self.subtitulo.get_size()[0] // 2
            py = (0.2 * ConfigJogo.ALTURA_TELA // 2) + \
                 (self.titulo.get_size()[1] * 1.5)
            tela.blit(self.subtitulo, (px, py))

    def desenha_subtitulo_2(self, tela):
        px = ConfigJogo.LARGURA_TELA // 2 - \
             self.subtitulo_2.get_size()[0] // 2
        py = (0.2 * ConfigJogo.ALTURA_TELA // 2) + \
             (self.subtitulo.get_size()[1] * 4.5)
        tela.blit(self.subtitulo_2, (px, py))
