#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc
dado = float(input('Informe um número real qualquer: '))
porcaoInteira = trunc(dado)
print('O número {} tem a porção inteira de {}'.format(dado, porcaoInteira))