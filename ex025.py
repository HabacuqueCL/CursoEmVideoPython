#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

#nome = input('Digite o nome de uma pessoa: ').upper().split()
#verificaNome = 'SILVA' in nome
#print('Seu nome tem Silva? {}'.format(verificaNome))


#Resolução guanabara
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))