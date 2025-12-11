#09 Faça um programa de leia um número inteiro qualquer e mostre na tela a sua tabuada.
valor = int(input('Insira um valor: '))
mult1 = valor * 1
mult2 = valor * 2
mult3 = valor * 3
mult4 = valor * 4
mult5 = valor * 5
mult6 = valor * 6
mult7 = valor * 7
mult8 = valor * 8
mult9 = valor * 9

print('#'+('-'*21)+'#')
print('| A tabuada do {} é: \n| {}x1 = {}  \n| {}x2 = {}  \n| {}x3 = {} \n| {}x4 = {} \n| {}x5 = {} \n| {}x6 = {} \n| {}x7 = {} \n| {}x8 = {}  \n| {}x9 = {}'.format(valor,valor,mult1,valor,mult2,valor,mult3,valor,mult4,valor,mult5,valor,mult6,valor,mult7,valor,mult8,valor,mult9))
print('#'+('-'*21)+'#')

