import random


def forca():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    jogo = True
    #Define o tema
    while jogo:

        print("Escolha um tema:")
        print("1- Objetos")
        print("2- Frutas")
        print("3- Nomes Masculino")
        print("4- Nomes Feminino")
        
        tema = int(input()) 

        if tema == 1:
            arquivo = open("Objetos.txt", "r")
        elif tema == 2:
            arquivo = open("Frutas.txt", "r")
        elif tema == 3:
            arquivo = open("Nomes Masculino.txt", "r")
        elif tema == 4:
            arquivo = open("Nomes Feminino.txt", "r")
        else:
            print("opção invalida")
            continue

    #Define a palavra secreta
        lista = []

        for linha in arquivo:
            linha = linha.strip()
            lista.append(linha)
        arquivo.close

        palavra_aleatoria = random.randrange (0, len(lista))
        palavra_seceta = lista [palavra_aleatoria]
        #print(palavra_seceta)

        
    #Inicio do jogo (quantidade de chances + print inicial da palavra oculta)
        chances = 7
        print(f"A palavra secreta possui {len(palavra_seceta)} letras.\n         E você possui {chances} chances")
        chutes_certos =  ["_"for letra in palavra_seceta]
        print(chutes_certos)


    #Chuetes do usuario
        print ("digite uma letra")
        
        letra_acertadas=[]

        while chances >0:
            chute = input()
            chute = chute.strip().lower()
            letra_acertadas.append(chute)

    #chute certo
            if chute in palavra_seceta:
                print (f"A palavra secreta possui '{chute}'")
                index = 0
                for letra in palavra_seceta:
                    if chute == letra:
                        chutes_certos[index] = letra
                    index += 1 
                print(chutes_certos)

    #chutes errado
            else:
                print(f"A palavra secreta nao possui '{chute}'\n      Tente de novo")
                letra_acertadas.remove(chute)
                chances -= 1
            print(f"digite uma nova letra\nAgora você possui {chances} chances")

    # Validando se palavra secreta esta correta
            temp = ""
            for count in palavra_seceta:
                if count in letra_acertadas:
                    temp += count

            if temp == palavra_seceta:
                print("vc ganhou!")
                break

            if chances == 0:
                print("voce perdeu")

    #continuar o jogo
        jogo = int(input("Deseja jovar novamente:\n 1- sim \n 2- não"))
        if jogo == 1:
            jogo = True
        else:
            jogo = False

if __name__ == "__main__":
    forca()
