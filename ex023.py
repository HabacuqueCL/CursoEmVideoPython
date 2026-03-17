#Faca um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#EX: Digite um número: 1834

#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

#Identificando como string
n = input('Digite um número de 0 a 9999: ')
s = '000' + n
print('Unidade: {}'.format(s[-1]))
print('Dezena: {}'.format(s[-2]))
print('Centena: {}'.format(s[-3]))
print('Milhar: {}'.format(s[-4]))

#Identificando via calculo matemático
#num = int(input('Digite um número de 0 a 9999: '))
#unidade = num % 10
#dezena = (num // 10) % 10
#centena = (num // 100) % 10
#milhar = (num // 1000) % 10
#print('Unidade: {}'.format(unidade))
#print('Dezena: {}'.format(dezena))
#print('Centena: {}'.format(centena))
#print('Milhar: {}'.format(milhar))