
class Personagem:
    def __init__(self, idade, raca, classe):
        self.idade = idade
        self.raca = raca
        self.classe = classe

class Mago:
    def __init__(self, idade, raca, classe, vida, mana):
        super(Personagem).__init__()
        self.idade = idade
        self.raca = raca
        self.classe = classe
        self.vida = vida
        self.mana = mana


print("======= Criação de personagem ======\n")
nome = input("Qual será seu nome?\n")
idade = int(input("Qual a sua idade?\n"))
raca = input("Qual a sua raça?\n")
classe = int(input("Escolha uma classe: 1- Guerreiro 2- Arqueiro 3- Mago\n"))

if classe == 3:
    Personagem = Mago(idade, raca, classe, 100, 100)
    print("Personagem criado")
    classe = "mago"
    print(f"\n\nNome: {nome}\n\n idade:{idade}\n\n Raça:{raca}\n\n classe: {classe}\n\n Vida: {100}\n\n Mana:{100}\n\n\n\n")

print("Você acorda...")
print("Você se encontra em frente a uma masmorra...")
print("Você entra?")

print("======= Criação de personagem ======\n")
nome = input("Qual será seu nome?\n")
idade = int(input("Qual a sua idade?\n"))
raca = input("Qual a sua raça?\n")
classe = int(input("Escolha uma classe: 1- Guerreiro 2- Arqueiro 3- Mago\n"))

class Guerreiro :
    def __init__(self, idade, raca, classe, vida):
        super(Personagem).__init__()
        self.idade = idade
        self.raca = raca
        self.classe = classe
        self.vida = vida


        if classe == 1:
