#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas

nome = input('Digite seu nome: ')
print('Olá',nome,'. Seja bem vindo!')

nome = input('Digite seu nome: ')
print('Ola {}! Seja bem vindo!'.format(nome))

#Crie um script Python que leia o dia, o mês e o ano de uma pessoa e mostre uma mensagem com a data formatada

dia = input('Digite o dia: ')
mes = input('Digite o mês: ')
ano = input('Digite o ano: ')
print('A data inserida foi:',dia,'de',mes,'de',ano,'.')

#Crie um script Python que leia dois números e tente mostrar a soma entre eles.

num1 = int(input('Insira um número:'))
num2 = int(input('Insira outro número:'))
soma = num1+num2
print('A soma dos dois numero é',soma)


#Tipos primitivos
#int = 7, -4, 0, 9875
#float = 4.5, 0.0076, -15.223, 7.0
#bool = true or false
#str = 'Olá', '7.5', ''