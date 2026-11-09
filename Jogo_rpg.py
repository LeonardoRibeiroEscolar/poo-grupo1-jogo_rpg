class Personagem:
    def __init__(self, idade, raca, classe):
        self.idade = idade
        self.raca = raca
        self.classe = classe

class Mago:
    def __init__(self, idade, raca, classe, vida):
        super(Personagem).__init__()
        self.idade = idade
        self.raca = raca
        self.classe = classe
        self.vida = vida


print("======= Criação de personagem ======\n")
nome = input("Qual será seu nome?\n")
idade = int(input("Qual a sua idade?\n"))
raca = input("Qual a sua raça?\n")
classe = int(input("Escolha uma classe: 1- Guerreiro 2- Arqueiro 3- Mago\n"))



mago = Mago(45, "humano", 100)
