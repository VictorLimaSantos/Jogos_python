import random
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")


def adivinhacao():
    numero_secreto = random.randint(1, 50)

    tentativas = 5

    while tentativas >= 0:
        print("digite um numero")
        chute = int(input())
        print(f"voce possui {tentativas} tentativas")

        if chute == numero_secreto:
            print("Parabens você acertou!")
            break 
        elif chute < numero_secreto and tentativas > 0:
            print("Tente um numero maior!")
            tentativas -= 1
            continue
        elif chute > numero_secreto and tentativas > 0:
            print("Tente um numero menor!")
            tentativas -= 1
            continue
        elif tentativas == 0:
            print(f"acabaram as chances! o nuemro secreto é {numero_secreto}")
            break


if __name__ == "__main__":
    adivinhacao()
