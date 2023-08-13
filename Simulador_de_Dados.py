import random


def dados():
    print("**************************************")
    print("***Bem vindo ao simulador de DADOS!***")
    print("**************************************")

    qtd_dados = int(input("quantos dados deseja adicionar?"))
    qtd_faces = int(input("seram dados de quantas faces?"))

    jogar_novamente = 1

    while jogar_novamente == 1:
        resultado = int
        qtd_dados = int(input("quantos dados deseja adicionar?"))
        qtd_faces = int(input("seram dados de quantas faces? \nD4 \nD6 \nD8 \nD10 \nD12 \nD20\n"))
        resultado = 0

        while qtd_dados < 0 or qtd_faces <= 1:
            print("Valor invalido, tente novamente:")
            qtd_dados = int(input("quantos dados deseja adicionar?"))
            qtd_faces = int(input("\nseram dados de quantas faces?"))
            
        print(f"O dado selecionado possui {qtd_faces} faces e você ira jogar {qtd_dados} dados")

        index = 1
        while qtd_dados >0:

            dado = random.randrange (1 , qtd_faces +1)
            print(f"rolou o dado {index}, o resultado foi {dado}")

            resultado = resultado + dado
            qtd_dados -= 1
            index += 1

        print(f"a soma dos dados foi {resultado}")

        jogar_novamente = int(input("Deseja Jogar novamente?\n1- Sim\n2- Não\n"))


if __name__ == "__main__":
    dados()




