from palavras import sorteio


def forca():
    palavra = sorteio()
    letras_lista = []
    vidas = 5
    ganhou = False
    pontos = 0

    while True:
        for letra in palavra:
            if letra in letras_lista:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        print(" ")
        tentativas = input("tente adivinhar uma letra!:").lower()
        letras_lista.append(tentativas)
        if tentativas not in palavra:
            vidas -= 1
            print(f"você tem {vidas} tentativas!")

        ganhou = True
        for letra in palavra:
            if letra not in letras_lista:
                ganhou = False

        if vidas == 0 or ganhou:
            break

    if ganhou:
        pontos += 1
        print(f"parabéns você ganhou e recebeu {pontos} ponto!")
        print(f"a palavra era {palavra}")
    else:
        print(f"você perdeu! a palavra era {palavra}!")


input("S para continuar ou qualquer tecla para sair:")

while True:
    forca()
    continuar = input(
        "\nDigite 's' para jogar novamente ou qualquer outra tecla para sair: ").lower()
    if continuar != 's':
        print("Obrigado por jogar! Até a próxima.")
        break
