#Faca um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR. 

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print('Numeros inseridos {}, {}, {}. O maior é {} e o menor é {}.'.format(num1, num2, num3, maior, menor))