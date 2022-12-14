from minions import Minions
from config_personagem import Personagem


class Vetor(Personagem, Minions):
    Personagem.__init__(posicao)
    Minions.__init__(posicao)
