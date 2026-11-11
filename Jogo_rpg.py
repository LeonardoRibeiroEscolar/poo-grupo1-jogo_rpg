import random

# Classe principal
class Personagem:
    def __init__(self, idade, raca, classe):
        self.idade = idade
        self.raca = raca
        self.classe = classe


# Classe Mago
class Mago(Personagem):
    def __init__(self, idade, raca, classe, vida, mana):
        super().__init__(idade, raca, classe)
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


# Classe Guerreiro
class Guerreiro(Personagem):
    def __init__(self, idade, raca, classe, vida):
        super().__init__(idade, raca, classe)
        self.vida = vida

    def atacar(self):
        print("Você atacou com sua espada!")
        return 20


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


# Criação de personagem
print("====== Criação de personagem ======\n")

nome = input("Qual será seu nome?\n")
idade = int(input("Qual a sua idade?\n"))
raca = input("Qual a sua raça?\n")

print("\nEscolha uma classe:")
print("1- Guerreiro")
print("2- Arqueiro")
print("3- Mago")

classe = int(input("Digite o número da classe: "))

# Escolha da classe
if classe == 1:
    personagem = Guerreiro(idade, raca, "Guerreiro", 120)


elif classe == 2:
    personagem = Arqueiro(idade, raca, "Arqueiro", 100, 30)


elif classe == 3:
    personagem = Mago(idade, raca, "Mago", 100, 100)


else:
    print("Classe inválida!")
    exit()

# Informações do personagem
print("\n====== Personagem criado ======")
print(f"Nome: {nome}")
print(f"Idade: {personagem.idade}")
print(f"Raça: {personagem.raca}")
print(f"Classe: {personagem.classe}")
print(f"Vida: {personagem.vida}")

if isinstance(personagem, Mago):
    print(f"Mana: {personagem.mana}")

if isinstance(personagem, Arqueiro):
    print(f"Flechas: {personagem.flechas}")

# Início da aventura
print("\nVocê acorda...")
print("Você se encontra em frente a uma masmorra...")

entrar = input("Você entra? (sim/não): ").lower()

if entrar == "sim":

    print("\nVocê entrou na masmorra!")
    print("Um monstro apareceu!")

    vida_monstro = 80

    # Sistema de batalha
    while personagem.vida > 0 and vida_monstro > 0:

        print("\n====== Batalha ======")
        print(f"Sua vida: {personagem.vida}")
        print(f"Vida do monstro: {vida_monstro}")

        print("\n1- Atacar")
        print("2- Ver status")
        print("3- Fugir")

        escolha = input("Escolha uma ação: ")

        if escolha == "1":

            dano = personagem.atacar()
            vida_monstro -= dano

            if vida_monstro < 0:
                vida_monstro = 0

            print(f"Dano causado: {dano}")

            if vida_monstro <= 0:
                print("\nVocê derrotou o monstro!")
                print("Parabéns, você venceu!")
                break

            # Ataque do monstro
            dano_monstro = random.randint(5, 15)
            personagem.vida -= dano_monstro

            print(f"O monstro atacou você!")
            print(f"Dano recebido: {dano_monstro}")


        elif escolha == "2":

            print("\n====== Status ======")
            print(f"Nome: {nome}")
            print(f"Classe: {personagem.classe}")
            print(f"Vida: {personagem.vida}")

            if isinstance(personagem, Mago):
                print(f"Mana: {personagem.mana}")

            if isinstance(personagem, Arqueiro):
                print(f"Flechas: {personagem.flechas}")


        elif escolha == "3":
            print("\nVocê fugiu da masmorra!")
            break


        else:
            print("Opção inválida!")

    if personagem.vida <= 0:
        print("\nVocê morreu!")
        print("Fim de jogo!")


else:
    print("\nVocê decidiu não entrar na masmorra.")
    print("Fim de jogo!")
    self.mana = mana