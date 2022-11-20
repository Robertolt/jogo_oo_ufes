from pygame import Surface
import pygame

from config_jogo import ConfigJogo
from cronometro import Cronometro


class EstadoJogo:
    def __init__(self):
        # salvamos a fonte para nao precisar criar ela toda hora
        self.font = pygame.font.SysFont(None, 24)
        # cronometro para medir o tempo de jogo
        self.cronometro = Cronometro()
        # reinicia o numero de goals e o tempo.
        self.resetar()

    def resetar(self):
        self.cronometro.reset()

    def jogo_terminou(self):
        if self.cronometro.tempo_passado() > ConfigJogo.DURACAO_PARTIDA:
            return True
        else:
            return False

    def desenha(self, tela: Surface):
        self.desenha_placar(tela)
        self.desenha_tempo(tela)

    def desenha_placar(self, tela: Surface):
        g1 = 2
        g2 = 2
        img = self.font.render(f'{g1} x {g2}', True, ConfigJogo.COR_ESTADO)
        px = ConfigJogo.LARGURA_TELA // 2 - img.get_size()[0] // 2
        py = ConfigJogo.ALTURA_PLACAR
        tela.blit(img, (px, py))

    def desenha_tempo(self, tela: Surface):
        tempo = ConfigJogo.DURACAO_PARTIDA - self.cronometro.tempo_passado()
        img = self.font.render(f'{tempo:.0f}',
                               True, ConfigJogo.COR_ESTADO)
        px = ConfigJogo.LARGURA_TELA // 2 - img.get_size()[0] // 2
        py = ConfigJogo.ALTURA_TEMPO
        tela.blit(img, (px, py))