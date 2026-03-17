#Crie um programa que leia o nome completo der uma pessoa e mostre:
#O nome com todas as letras maiusculas.
#O nome com todas minusculas.
#Quantas letras ao todo (Sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = input('Digite o seu nome completo: ')
retirarEspacos = nome.replace(' ','')
dividir = nome.split()
print('Seu nome em maiusculo: {}'.format(nome.upper()))
print('Seu nome em minusculo: {}'.format(nome.lower()))
print('Seu nome possui {} letras no total.'.format(len(retirarEspacos)))
print('Seu primeiro nome tem {} letras.'.format((len(dividir[0]))))