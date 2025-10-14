#Crie um programa que leia dois números e mostre a soma entre eles.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
soma = num1 + num2
print('A soma dos números é: {}'.format(soma))

#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

dado = input('Digite algo: ')
print('Esse dado é alfa númerico:',dado.isalnum())
print('Esse dado é alfabetico:',dado.isalpha())
print('Esse dado é decimal:',dado.isdecimal())
print('Esse dado está todo em letra minuscula:',dado.islower())
print('Esse dado é númerico:',dado.isnumeric())
print('Esse dado está todo em letra maiuscula:',dado.isupper())