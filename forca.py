def jogar():
    print("=================================")
    print("== Bem vindo ao jogo de Forca! ==")
    print("=================================")

    palavra_secreta = "paralelepipedo".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    tentativas = 0

    print(letras_acertadas)

    while(not acertou and not enforcou):

        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            posicao = 0
            for letra in (palavra_secreta):
                if(chute == letra):
                    letras_acertadas[posicao] = letra
                posicao += 1
        else:
            tentativas +=1

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!!!")
    else:
        print("Você perdeu!!!")
    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()