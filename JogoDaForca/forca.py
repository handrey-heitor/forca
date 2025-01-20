from palavras import palavra


def forca(): 
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
    tentativas = input("tente adivinhas uma letra!:").lower()
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

    
forca()



