import random

# ============================================
# classe mãe personagem
# ============================================
class Personagem:
    def __init__(self, nome, idade, raca, classe, vida):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.classe = classe
        self.__vida = vida


    @property
    def vida(self):
        return self.__vida


    def receber_dano(self, dano):
        if dano > 0:
            self.__vida = max(0, self.__vida - dano)


    def esta_vivo(self):
        return self.__vida > 0


    def mostrar_status(self):
        print("\n====== Status ======")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Raça: {self.raca}")
        print(f"Classe: {self.classe}")
        print(f"Vida: {self.vida}")

# =====================================
# Classe filha Mago
# =====================================


class Mago(Personagem):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade, raca, "Mago", 100)
        self.__mana = 100


    @property
    def mana(self):
        return self.__mana


    def atacar(self):
        if self.__mana >= 10:
            self.__mana -= 10
            print("Você lançou uma bola de fogo!")
            return 25
        else:
            print("Mana insuficiente!")
            return 0


    def mostrar_status(self):
        super().mostrar_status()
        print(f"Mana: {self.mana}")




# =====================================
# Classe filha Guerreiro
# =====================================


class Guerreiro(Personagem):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade, raca, "Guerreiro", 120)


    def atacar(self):
        print("Você atacou com sua espada!")
        return 20




# =====================================
# Classe filha Arqueiro
# =====================================


class Arqueiro(Personagem):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade, raca, "Arqueiro", 100)
        self.__flechas = 30


    @property
    def flechas(self):
        return self.__flechas


    def atacar(self):
        if self.__flechas > 0:
            self.__flechas -= 1
            print("Você disparou uma flecha!")
            print(f"Flechas restantes: {self.flechas}")
            return 20
        else:
            print("Você está sem flechas!")
            return 0


    def mostrar_status(self):
        super().mostrar_status()
        print(f"Flechas: {self.flechas}")




# =====================================
# Classe Gerenciadora de personagens
# =====================================


class GerenciadorPersonagens:
    def __init__(self):
        self.__personagens = []


    def criar_personagem(self, nome, idade, raca, classe):


        if classe == 1:
            personagem = Guerreiro(nome, idade, raca)


        elif classe == 2:
            personagem = Arqueiro(nome, idade, raca)


        elif classe == 3:
            personagem = Mago(nome, idade, raca)


        else:
            print("Classe inválida!")
            return None


        self.__personagens.append(personagem)
        print("\nPersonagem criado com sucesso!")
        return personagem


    def listar_personagens(self):
        print("\n====== Personagens ======")


        if not self.__personagens:
            print("Nenhum personagem cadastrado.")
            return


        for personagem in self.__personagens:
            print(f"{personagem.nome} - {personagem.classe}")


    def quantidade_personagens(self):
        return len(self.__personagens)




# =====================================
# Classe Gerenciador de Batalha
# =====================================


class GerenciadorBatalha:
    def __init__(self, personagem):
        self.personagem = personagem
        self.__vida_monstro = 80


    def iniciar_batalha(self):


        print("\nVocê entrou na masmorra!")
        print("Um monstro apareceu!")


        while self.personagem.esta_vivo() and self.__vida_monstro > 0:


            print("\n====== Batalha ======")
            print(f"Sua vida: {self.personagem.vida}")
            print(f"Vida do monstro: {self.__vida_monstro}")


            print("\n1- Atacar")
            print("2- Ver status")
            print("3- Fugir")


            escolha = input("Escolha uma ação: ")


            if escolha == "1":


                dano = self.personagem.atacar()
                self.__vida_monstro = max(
                    0, self.__vida_monstro - dano
                )


                print(f"Dano causado: {dano}")


                if self.__vida_monstro <= 0:
                    print("\nVocê derrotou o monstro!")
                    print("Parabéns, você venceu!")
                    break


                dano_monstro = random.randint(5, 15)
                self.personagem.receber_dano(dano_monstro)


                print("O monstro atacou você!")
                print(f"Dano recebido: {dano_monstro}")


            elif escolha == "2":
                self.personagem.mostrar_status()


            elif escolha == "3":
                print("\nVocê fugiu da masmorra!")
                break


            else:
                print("Opção inválida!")


        if not self.personagem.esta_vivo():
            print("\nVocê morreu!")
            print("Fim de jogo!")


def main():


    gerenciador = GerenciadorPersonagens()

# Criação de personagem com perguntas(print/input)

    print("====== Criação de personagem ======\n")


    nome = input("Qual será seu nome?\n")
    idade = int(input("Qual a sua idade?\n"))
    raca = input("Qual a sua raça?\n")


    print("\nEscolha uma classe:")
    print("1- Guerreiro")
    print("2- Arqueiro")
    print("3- Mago")


    classe = int(input("Digite o número da classe: "))


    personagem = gerenciador.criar_personagem(
        nome, idade, raca, classe
    )


    if personagem is None:
        return


    print("\n====== Personagem criado ======")
    personagem.mostrar_status()


    print("\nVocê acorda...")
    print("Você se encontra em frente a uma masmorra...")


    entrar = input("Você entra? (sim/não): ").lower()


    if entrar == "sim":
        batalha = GerenciadorBatalha(personagem)
        batalha.iniciar_batalha()


    else:
        print("\nVocê decidiu não entrar na masmorra.")
        print("Fim de jogo!")




if __name__ == "__main__":
    main()