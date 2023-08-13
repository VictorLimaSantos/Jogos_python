import Advinhacao
import Cartas_21
import Forca
import Jokenpo
import Simulador_de_Dados

print("*********************************")
print("*********Menu de seleção*********")
print("*********************************")

print("Jogos disponiveis:\n 1- Adivinhação\n 2- Cartas 21\n 3- Forca \n 4- Jokenpo\n 5- Simulador de dados")
op = int(input("Selecione uma Opção: "))

if op == 1:
    print("Selecionado Opção 1:\n Jogo de Adivinhação")
    Advinhacao.adivinhacao()
elif op == 2:
    print("Selecionado Opção 2:\n Jogo de Cartas 21")
    Cartas_21.cartas()
elif op == 3:
    print("Selecionado Opção 3:\n Jogo da Forca")
    Forca.forca()
elif op == 4:
    print("Selecionado Opção 4:\n Jogo de Jokenpo")
    Jokenpo.jokenpo()
elif op == 5:
    print("Selecionado Opção 5:\n Simulador de dados")
    Simulador_de_Dados.dados()
