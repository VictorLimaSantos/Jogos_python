import random


def jokenpo():
    print("********************************")
    print("***Bem vindo ao jogo Jokenpo!***")
    print("********************************")

    qtd_rodadas = int(input("selecione a quantidade de rodadas: "))
    jog = 0
    maq = 0

    while qtd_rodadas >0:
        qtd_rodadas -= 1
        maquina = random.randrange(1 , 5)
        maquina1 = maquina
        
        print("\nEscolha uma opção:\n 1- Tesoura\n 2- Papel\n 3- Pedra\n 4- Largato\n 5- Spock")
        jogador = int(input())

        if jogador == maquina1:
            print('Empate')
            continue

        if jogador == 1 and (maquina1 == 2 or maquina1 == 4):
            if maquina1 == 2:
                print('Tesoura corta Papel')
                print('Você Ganhou')
            elif maquina1 == 4:
                print('Tesoura decapta Largato')
                print('Você Ganhou')
            jog += 1
        elif jogador == 2 and (maquina1 == 3 or maquina1 == 5):
            if maquina1 == 3:
                print('Papel cobre Pedra')
                print('Você Ganhou')
            elif maquina1 == 5:
                print('Papel refuta Spock')
                print('Você Ganhou')
            jog += 1
        elif jogador == 3 and (maquina1 == 4 or maquina1 == 1):
            if maquina1 == 4:
                print('Pedra esmaga Largato')
                print('Você Ganhou')
            elif maquina1 == 1:
                print('Pedra quebra Tesoura')
                print('Você Ganhou')
            jog += 1
        elif jogador == 4 and (maquina1 == 5 or maquina1 == 2):
            if maquina1 == 5:
                print('Largato envenena Spock')
                print('Você Ganhou')
            elif maquina1 == 2:
                print('Largato come Papel')
                print('Você Ganhou')
            jog += 1
        elif jogador == 5 and (maquina1 == 3 or maquina1 == 1):
            if maquina1 == 3:
                print('Spock esmaga Pedra')
                print('Você Ganhou')
            elif maquina1 == 1:
                print('Spock Quebra tesoura')
                print('Você Ganhou')
            jog += 1

        else:
            if maquina1 == 1 and (jogador == 2 or jogador == 4):
                if jogador == 2:
                    print('Tesoura corta Papel')
                    print('Maquina Ganhou')
                elif jogador == 4:
                    print('Tesoura decapta Largato')
                    print('Maquina Ganhou')
                maq +=1
            elif maquina1 == 2 and (jogador == 3 or jogador == 5):
                if jogador == 3:
                    print('Papel cobre Pedra')
                    print('Maquina Ganhou')
                elif jogador == 5:
                    print('Papel refuta Spock')
                    print('Maquina Ganhou')
                maq +=1
            elif maquina1 == 3 and (jogador == 4 or jogador == 1):
                if jogador == 4:
                    print('Pedra esmaga Largato')
                    print('Maquina Ganhou')
                elif jogador == 1:
                    print('Pedra quebra Tesoura')
                    print('Maquina Ganhou')
                maq +=1
            elif maquina1 == 4 and (jogador == 5 or jogador == 2):
                if jogador == 5:
                    print('Largato envenena Spock')
                    print('Maquina Ganhou')
                elif jogador == 2:
                    print('Largato come Papel')
                    print('Maquina Ganhou')
                maq +=1
            elif maquina1 == 5 and (jogador == 3 or jogador == 1):
                if jogador == 3:
                    print('Spock esmaga Pedra')
                    print('Maquina Ganhou')
                elif jogador == 1:
                    print('Spock Quebra tesoura')
                    print('Maquina Ganhou')
                maq +=1

            print ("\nMaquina selecionou", maquina1)

        print (f'\nJogador marcou {jog} pontos')
        print (f'Maquina marcou {maq} pontos')


if __name__ == "__main__":
    jokenpo()