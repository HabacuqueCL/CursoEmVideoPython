"""Crie um programa que leia o nome completo der uma pessoa e mostre:
#O nome com todas as letras maiusculas.
#O nome com todas minusculas.
#Quantas letras ao todo (Sem considerar espaços).
#Quantas letras tem o primeiro nome."""

nome = 'Habacuque Cavalcante Leal'
print('Seu nome em maiusculo: {}'.format(nome.upper()))
print('Seu nome em minusculo: {}'.format(nome.lower()))
dividir = nome.split()
print('Quantas letras tem seu nome: {}'.format(dividir.len([0])))