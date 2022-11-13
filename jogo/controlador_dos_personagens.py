# esse py é responsável pelo controle dos personagens. Logo o jogador é controlado
# AWSD e o jogador2 pelo IJKL

class Jogador1:
    def __init__(self, posicao):
        self.posicao = posicao
        self.velocidade = 0

    def mover_pra_cima(self):
        self.velocidade = -ConfigJogo.VELOCIDADE_PERSONAGEM_Y

    def mover_pra_baixo(self):
        self.velocidade = ConfigJogo.VELOCIDADE_PERSONAGEM_Y

    def mover_pra_esquerda(self):
        self.velocidade = -ConfigJogo.VELOCIDADE_PERSONAGEM_X

    def mover_pra_direita(self):
        self.velocidade = ConfigJogo.VELOCIDADE_PERSONAGEM_X

    def parar(self):
        self.velocidade = 0

    def atualizar_posicao_x(self):
        x, y = self.posicao
        novo_x = x + self.velocidade_x
        self.posicao = (novo_x, y)
        if (0 >= novo_x) or (novo_x >= ConfigJogo.LARGURA_TELA):
            self.velocidade_x = - self.velocidade_x

    def atualizar_posicao_y(self):
        x, y = self.posicao
        novo_y = y + self.velocidade_y
        self.posicao = (x, novo_y)
        if (0 >= novo_y) or (novo_y >= ConfigJogo.ALTURA_TELA):
            self.velocidade_y = -self.velocidade_y

