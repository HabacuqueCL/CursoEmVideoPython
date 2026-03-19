#Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente

nome = input('Insira o seu nome: ')
splitNome = nome.split()
print('Primeiro nome: {}'.format(splitNome[0]))
print('Último nome: {}'.format(splitNome[-1]))