from personagem import Personagem
# Criação da classe filha "Arqueiro" e ele herda atributos da classe mãe
class Arqueiro(Personagem):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade, raca, "Arqueiro", 100)
        self.__flechas = 30


    @property
    def flechas(self):
        return self.__flechas

# Criação do metodo ataque para o Arqueiro, ele usa polimorfismo para funcionar de forma diferente em cada classe filha
    def atacar(self):
        if self.__flechas > 0:
            self.__flechas -= 1
            print("Você disparou uma flecha!")
            print(f"Flechas restantes: {self.flechas}")
            return 20
        else:
            print("Você está sem flechas!")
            return 0

# mostrar status
    def mostrar_status(self):
        super().mostrar_status()
        print(f"Flechas: {self.flechas}")


