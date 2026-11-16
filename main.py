
#Criação do menu principal(iniciar o jogo e sair)
resposta = 0
print("===== BEM VINDO AO JOGO =====")
print(" pressione 1- iniciar")
print(" pressione 2- sair")

int(input(resposta))
print("\n\n\n")
if resposta == 2:
    print("FIM DE JOGO")
    exit()

from  classes import personagem
from  classes import mago
from  classes import arqueiro
from  classes import guerreiro
