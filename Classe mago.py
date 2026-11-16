
#Criação da classe filha "Mago" e ele herda atributos da classe mãe
class Mago:
    def __init__(self, idade, raca, classe, vida, mana):
        super(Personagem).__init__()
        self.idade = idade
        self.raca = raca
        self.classe = classe
        self.vida = vida
        self.mana = mana

# Criação do metodo ataque para o Mago, ele usa polimorfismo para funcionar de forma diferente em cada classe filha
    def atacar(self):
        if self.mana >= 10:
            self.mana -= 10
            print("Você lançou uma bola de fogo!")
            return 25
        else:
            print("Mana insuficiente!")
            return 0
            

