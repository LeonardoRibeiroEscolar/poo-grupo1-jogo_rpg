
class Arqueiro(Personagem):
    def __init__(self, idade, raca, classe, vida, flechas):
        super().__init__(idade, raca, classe)
        self.vida = vida
        self.flechas = flechas
        self.dano = 20


    def atacar(self):
        if self.flechas > 0:
            self.flechas -= 1
            print("Você disparou uma flecha!")
            print(f"Dano causado: {self.dano}")
            print(f"Flechas restantes: {self.flechas}")
        else:
            print("Você está sem flechas!")


    def status(self):
        print(f"Vida: {self.vida}")
        print(f"Flechas: {self.flechas}")
        print(f"Dano: {self.dano}")

        classe = int(input("Escolha uma classe: 1- Guerreiro 2- Arqueiro 3- Mago\n"))

        if classe == 2:
            personagem = Arqueiro(idade, raca, classe, 100, 30)
            print("Personagem criado")
            classe = "arqueiro"

            print(f"\nNome: {nome}")
            print(f"Idade: {idade}")
            print(f"Raça: {raca}")
            print(f"Classe: {classe}")
            print(f"Vida: {personagem.vida}")
            print(f"Flechas: {personagem.flechas}")

            if classe == "arqueiro":
                print("\nUm monstro apareceu!")

                while personagem.vida > 0:
                    print("\n1- Atacar")
                    print("2- Ver status")
                    print("3- Fugir")

                    escolha = input("Escolha uma ação: ")

                    if escolha == "1":
                        personagem.atacar()


                    elif escolha == "2":
                        personagem.status()


                    elif escolha == "3":
                        print("Você fugiu da batalha!")
                        break


                    else:
                        print("Opção inválida!")

                        class Mago:
                            def __init__(self, idade, raca, classe, vida, mana):
                                super(Personagem).__init__()

                        class Mago(Personagem):
                            def __init__(self, idade, raca, classe, vida, mana):
                                super().__init__(idade, raca, classe)
                                self.vida = vida
                                self.mana = mana