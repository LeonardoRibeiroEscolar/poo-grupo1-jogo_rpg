
# Classe Arqueiro
class Arqueiro(Personagem):
    def __init__(self, idade, raca, classe, vida, flechas):
        super().__init__(idade, raca, classe)
        self.vida = vida
        self.flechas = flechas
