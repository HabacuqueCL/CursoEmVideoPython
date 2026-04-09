#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem formar um triângulo ou não.

n1 = input('Valor 1: ')
n2 = input('Valor 2: ')
n3 = input('Valor 3: ')
if n1+n2>n3 and n1+n3>n2 and n2+n3>n1:
    print('É possível formar um triângulo com as retas informadas.')
else:
    print('Não é possível formar um triângulo com as retas informadas.')