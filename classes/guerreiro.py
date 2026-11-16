from personagem import Personagem
# Criação da classe filha "Guerreiro" e ele herda atributos da classe mãe
class Guerreiro :
    def __init__(self, idade, raca, classe, vida):
        super(Personagem).__init__()
        self.idade = idade
        self.raca = raca
        self.classe = classe
        self.vida = vida

# Criação do metodo ataque para o guerreiro, ele usa polimorfismo para funcionar de forma diferente em cada classe filha
        def atacar(self):
            print("Você atacou com sua espada!")
            return 20


