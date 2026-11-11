class Guerreiro :
    def __init__(self, idade, raca, classe, vida):
        super(Personagem).__init__()
        self.idade = idade
        self.raca = raca
        self.classe = classe
        self.vida = vida


        def atacar(self):
            print("Você atacou com sua espada!")
            return 20


