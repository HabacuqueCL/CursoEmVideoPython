#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "SANTO".

nomeCidade = input('Digite o nome da sua cidade: ')
palavra = 'SANTO'
if palavra in nomeCidade:
    print('O nome da cidade começa com SANTO')
else:
    print('O nome da cidade não começa com SANTO')