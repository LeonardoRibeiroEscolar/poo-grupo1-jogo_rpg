
# Classe Arqueiro
class Arqueiro(Personagem):
    def __init__(self, idade, raca, classe, vida, flechas):
        super().__init__(idade, raca, classe)
        self.vida = vida
        self.flechas = flechas




    def atacar(self):
        if self.flechas > 0:
            self.flechas -= 1
            print("Você disparou uma flecha!")
            print(f"Flechas restantes: {self.flechas}")
            return 20
        else:
            print("Você está sem flechas!")
            return 0

