#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

num = int(input('informe um número: '))
if num % 2 == 0:
    print('O número é PAR.')
else:
    print('O número é IMPAR.')
print('Fim da execução.')