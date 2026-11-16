from personagem import Personagem
# Criação da classe filha "Mago" e ele herda atributos da classe mãe
class Mago(Personagem):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade, raca, "Mago", 100)
        self.__mana = 100


    @property
    def mana(self):
        return self.__mana

# Criação do metodo ataque para o Mago, ele usa polimorfismo para funcionar de forma diferente em cada classe filha
    def atacar(self):
        if self.__mana >= 10:
            self.__mana -= 10
            print("Você lançou uma bola de fogo!")
            return 25
        else:
            print("Mana insuficiente!")
            return 0

    # mostrar status
    def mostrar_status(self):
        super().mostrar_status()
        print(f"Mana: {self.mana}")
