#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

informarNome = input('Digite o nome de uma pessoa: ')
verificarPalavra = 'SANTO'
if verificarPalavra in informarNome:
    print('Você tem a palavra SILVA no seu nome.')
else:
    print('Você não tem a palavra SILVA no seu nome.')    