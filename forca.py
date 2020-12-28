import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    adiciona_nova_palavra()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    while(not acertou and not enforcou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            tentativas +=1
            desenha_forca(tentativas)

        enforcou = tentativas == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def pede_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()
    return chute

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def imprime_mensagem_abertura():
    print("=================================")
    print("== Bem vindo ao jogo de Forca! ==")
    print("=================================")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("      _______________        ")
    print("     /               \       ")
    print("    /                 \      ")
    print("  //                   \/\   ")
    print("  \|   XXXX     XXXX   | /   ")
    print("   |   XXXX     XXXX   |/    ")
    print("   |   XXX       XXX   |     ")
    print("   |                   |     ")
    print("   \__      XXX      __/     ")
    print("     |\     XXX     /|       ")
    print("     | |           | |       ")
    print("     | I I I I I I I |       ")
    print("     |  I I I I I I  |       ")
    print("     \_             _/       ")
    print("       \_         _/         ")
    print("         \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]
    return palavra_secreta

def adiciona_nova_palavra():
    nova_palavra = input("Deseja adicionar uma nova palavra na lista de arquivos? responda: S ou N -> ")
    if(nova_palavra.strip().upper() == "S"):
        arquivo = open("palavras.txt", "a") # append
        arquivo.write(input("Digite a palavra: ") + "\n")
        arquivo.close()
        print("Nova palavra adicionada!")
    else:
        print("OK! Vamos lá.\n")

def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    posicao = 0
    for letra in (palavra_secreta):
        if (chute == letra):
            letras_acertadas[posicao] = letra
        posicao += 1

if(__name__ == "__main__"):
    jogar()