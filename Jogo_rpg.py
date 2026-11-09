class Personagem:
    def __init__(self, idade, raca):
        self.idade = idade
        self.raca = raca

class Mago:
    def __init__(self, idade, raca, vida):
        super(Personagem).__init__()
        self.idade = idade
        self.raca = raca
        self.vida = vida


print("======= Criação de personagem ======\n")
print("Qual será seu nome?")
input()
print("Qual a sua idade?")
input()
print("Qual a sua raça?")
input()
print("Escolha uma classe: 1- Guerreiro 2- Arqueiro 3- Mago")
input()


mago = Mago(45, "humano", 100)
