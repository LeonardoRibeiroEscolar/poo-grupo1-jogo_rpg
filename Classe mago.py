class Mago:
    def __init__(self, idade, raca, classe, vida, mana):
        super(Personagem).__init__()
        self.idade = idade
        self.raca = raca
        self.classe = classe
        self.vida = vida
        self.mana = mana


    def atacar(self):
        if self.mana >= 10:
            self.mana -= 10
            print("Você lançou uma bola de fogo!")
            return 25
        else:
            print("Mana insuficiente!")
            return 0

