from minions import Minions
from config_personagem import Personagem


class Vetor:
    def __init__(self, p, m):
        self.p = p
        self.m = m

    def calcular(self) -> float:
        xp, yp = self.p.posicao
        xm, ym = self.m.posicao
        x = (xp - xm) ** 2
        y = (yp - ym) ** 2
        resultado = (x + y) ** 0.5
        return resultado

