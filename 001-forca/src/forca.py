
import random as rd
import os
import tkinter as tki


janela = tki.Tk()
janela.title(string="Just Forca")
janela.mainloop()




# Escolhendo o assunto
print("""
Escolha um assunto para jogar

[0] Animais
[1] Frutas
""")

escolha_usr = int(input('Digite um numero correspondete a um assunto: '))
lista_assuntos = ['animais', 'frutas']
assunto = lista_assuntos[escolha_usr]


# Informando o caminho de onde estão os arquivos .txt
path_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_data = os.path.join(path_projeto, 'database', f'{assunto}.txt')


# Escolhendo a palavra relacionada ao assunto
with open(file=path_data, 
          mode='r', 
          encoding='utf-8') as arquivo:
    
    lista_palavras = arquivo.readlines()

palavra_escolhida = rd.sample(lista_palavras, 1)[0].strip('\n')


# Construindo o loop
palavra = ['_' for letra in palavra_escolhida]
vida = 3
tentativas_usr = []

while True:

    print(f'\nA palavra escolhida é: {palavra}')

    if '_' not in palavra:
        print('\nPARABÉNS, VOCÊ GANHOU\n')
        break

    letra_usr = input('Digite uma letra: ')

    if not(letra_usr.isalpha()):
        print('\nERRO, DIGITE APENAS LETRAS')
        continue

    if len(letra_usr) > 1:
        print('\nERRO, DIGITE APENAS UMA LETRA')
        continue

    if letra_usr in tentativas_usr:
        print('\nVOCÊ JÁ DIGITOU ESSA LETRA, TENTE OUTRA')
        continue
    else:
        tentativas_usr.append(letra_usr)

    if letra_usr in palavra_escolhida:
        for pos, letra in enumerate(palavra_escolhida):
            if letra_usr == letra:
                palavra[pos] = letra_usr

    else:
        vida-=1

        if vida == 0:
            print('\nVOCÊ PERDEU TODAS AS VIDAS, GAME OVER')
            break

        print(f'\nVOCÊ ERROU E AGORA SÓ TEM {vida} VIDA')



