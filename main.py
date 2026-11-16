import os
from personagem import main as iniciar_jogo

print("===== BEM VINDO AO JOGO =====")
print(" pressione 1- iniciar")
print(" pressione 2- sair")

resposta = input(">> ")

if resposta == "1":
    os.system("cls")
    iniciar_jogo()  # Executa toda a função main() do arquivo personagem.py

elif resposta == "2":
    print("FIM DE JOGO")
    exit()
else:
    print("Opção inválida!")