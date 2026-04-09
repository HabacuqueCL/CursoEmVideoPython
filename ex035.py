#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem formar um triângulo ou não.

n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
n3 = int(input('Valor 3: '))
maiorNum = max(n1,n2,n3)
if (n1+n2+n3)-maiorNum>maiorNum:
    print('É um triângulo.')
else:
    print('Não é um triângulo.')