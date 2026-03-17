#Faca um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#EX: Digite um número: 1834

#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

#Identificando como string
#num1 = input('Digite um número de 0 a 9999: ')
#joinNum = ' '.join(num1)
#splitNum = joinNum.split()
#print('Unidade: {}'.format(splitNum[3]))
#print('Dezena: {}'.format(splitNum[2]))
#print('Centena: {}'.format(splitNum[1]))
#print('Milhar: {}'.format(splitNum[0]))

#Identificando via calculo matemático
num = int(input('Digite um número de 0 a 9999: '))
unidade = num % 10
dezena = (num // 10) % 10
centena = (num // 100) % 10
milhar = (num // 1000) % 10
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))