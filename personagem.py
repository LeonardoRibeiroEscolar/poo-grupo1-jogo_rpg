class Personagem:
    def __init__(self, idade, raca, classe):
        self.idade = idade
        self.raca = raca
        self.classe = classe


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
print(f"Idade: {Personagem.idade}")
print(f"Raça: {Personagem.raca}")
print(f"Classe: {Personagem.classe}")
print(f"Vida: {Personagem.vida}")

if isinstance(Personagem, Mago):
    print(f"Mana: {Personagem.mana}")

if isinstance(Personagem, Arqueiro):
    print(f"Flechas: {Personagem.flechas}")

# Início da aventura
print("\nVocê acorda...")
print("Você se encontra em frente a uma masmorra...")


entrar = input("Você entra? (sim/não): ").lower()


if entrar == "sim":


    print("\nVocê entrou na masmorra!")
    print("Um monstro apareceu!")


    vida_monstro = 80


    # Sistema de batalha
    while Personagem.vida > 0 and vida_monstro > 0:


        print("\n====== Batalha ======")
        print(f"Sua vida: {Personagem.vida}")
        print(f"Vida do monstro: {vida_monstro}")


        print("\n1- Atacar")
        print("2- Ver status")
        print("3- Fugir")


        escolha = input("Escolha uma ação: ")


        if escolha == "1":


            dano = Personagem.atacar()
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
            Personagem.vida -= dano_monstro


            print(f"O monstro atacou você!")
            print(f"Dano recebido: {dano_monstro}")


        elif escolha == "2":


            print("\n====== Status ======")
            print(f"Nome: {nome}")
            print(f"Classe: {Personagem.classe}")
            print(f"Vida: {Personagem.vida}")


            if isinstance(Personagem, Mago):
                print(f"Mana: {Personagem.mana}")


            if isinstance(Personagem, Arqueiro):
                print(f"Flechas: {Personagem.flechas}")


        elif escolha == "3":
            print("\nVocê fugiu da masmorra!")
            break


        else:
            print("Opção inválida!")


    if Personagem.vida <= 0:
        print("\nVocê morreu!")
        print("Fim de jogo!")


else:
    print("\nVocê decidiu não entrar na masmorra.")
    print("Fim de jogo!")