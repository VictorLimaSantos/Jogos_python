import random


def cartas():
    print("*******************************")
    print("Bem vindo ao jogo de Cartas 21!")
    print("*******************************")

    #jogadores = {'jogador1': [],
    #'jogador2': []}

    jogar_novamente = 1

    while jogar_novamente == 1:

        carta_jogador = [(random.randrange(1,13)) , (random.randrange(1,13))]
        resultado = carta_jogador[0] + carta_jogador[1]

        if resultado < 21:

            print (f"Jogar iniciou com as cartas {carta_jogador[0]} e {carta_jogador[1]}, o total é de {resultado}\n")

            comprar_carta = int(input("deseja comprar mais uma carta?\n1- Sim\n2- Não\n"))

            while comprar_carta == 1:

                cartas_baralho = random.randrange (1 , 13)
                carta_jogador.append(cartas_baralho)
                resultado += cartas_baralho

                if resultado >21:
                    print(f"Jogardor puxou a carta {cartas_baralho} e agora tem as cartas {carta_jogador}\nA soma atual é de {resultado}")
                    print("ultrapassou o valor de 21, você perdeu!\n")
                    break

                elif resultado == 21:
                    print("resultado total de 21, Você ganhou!\n")
                    break

                print(f"Jogardor puxou a carta {cartas_baralho} e agora tem as cartas {carta_jogador}\n soma atual é de {resultado}")
                comprar_carta = int(input("deseja comprar mais uma carta?\n1- Sim\n2- Não\n"))

        elif resultado == 21:
            print("resultado total de 21, Você ganhou!\n")

        else:
            print("ultrapassou o valor de 21, você perdeu!\n")

        jogar_novamente = int(input("Deseja Jogar novamente?\n1- Sim\n2- Não\n"))


if __name__ == "__main__":
    cartas()