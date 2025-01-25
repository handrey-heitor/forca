import tkinter as tk
from tkinter import messagebox
import random


lista_de_palavras = ['azul', 'vermelho', 'cavalo', 'karma', 'caramelo', 'mar', 'rio', 'sol', 'lua', 'estrela']

def jogo_forca(palavra):
    def atualizar_palavra(letra):
        nonlocal vidas
        if letra in palavra:
            letras_certas.update([letra])
        else:
            letras_erradas.append(letra)
            vidas -= 1

        atualizar_interface()

        # Verifica condições de vitória ou derrota
        if "_" not in [letra if letra in letras_certas else "_" for letra in palavra]:
            fim_jogo("Parabéns, você venceu!")
        elif vidas == 0:
            fim_jogo(f"Você perdeu! A palavra era '{palavra}'.")

    def atualizar_interface():
        # Atualiza a exibição da palavra
        palavra_atual = " ".join([letra if letra in letras_certas else "_" for letra in palavra])
        label_palavra.config(text=palavra_atual)

        # Desativa as letras clicadas
        for btn in botoes:
            if btn["text"] in letras_certas or btn["text"] in letras_erradas:
                btn.config(state="disabled")

        # Atualiza as vidas restantes
        label_vidas.config(text=f"Vidas restantes: {vidas}")

        # Atualiza as letras erradas
        label_erradas.config(text=f"Letras erradas: {', '.join(letras_erradas)}")

    def fim_jogo(mensagem):
        # Mostra mensagem de vitória ou derrota
        continuar = messagebox.askyesno("Fim de Jogo", f"{mensagem}\nDeseja jogar novamente?")
        if continuar:
            janela.destroy()  # Fecha a janela atual
            rodar_jogo()  # Reinicia o jogo
        else:
            janela.destroy()  # Fecha a aplicação

    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Jogo da Forca")
    janela.geometry("500x500")

    # Letras certas e erradas
    letras_certas = set()
    letras_erradas = []
    vidas = 5

    # Label para exibir a palavra
    label_palavra = tk.Label(janela, text=" ".join(["_" for _ in palavra]), font=("Helvetica", 24))
    label_palavra.pack(pady=20)

    # Label para exibir as vidas restantes
    label_vidas = tk.Label(janela, text=f"Vidas restantes: {vidas}", font=("Helvetica", 14))
    label_vidas.pack(pady=10)

    # Label para exibir as letras erradas
    label_erradas = tk.Label(janela, text="Letras erradas: ", font=("Helvetica", 14), fg="red")
    label_erradas.pack(pady=10)

    # Frame para os botões do alfabeto
    frame_botoes = tk.Frame(janela)
    frame_botoes.pack()

    # Botões do alfabeto
    botoes = []
    for letra in "abcdefghijklmnopqrstuvwxyz":
        btn = tk.Button(frame_botoes, text=letra.upper(), width=4, height=2, 
                        command=lambda l=letra: atualizar_palavra(l))
        btn.pack(side="left", padx=2, pady=2)
        botoes.append(btn)

    # Inicializa a interface
    janela.mainloop()

def rodar_jogo():
    # Sorteia uma nova palavra a cada jogo
    palavra_sorteada = random.choice(lista_de_palavras)
    jogo_forca(palavra_sorteada)

# Inicia o jogo
rodar_jogo()
