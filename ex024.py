#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "SANTO".

nomeCidade = input('Digite o nome da sua cidade: ')
splitCidade = nomeCidade.split()
print('SANTO' in splitCidade[0])