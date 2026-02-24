#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

grupo1 = input('Informe o primeiro grupo: ')
grupo2 = input('Informe o segundo grupo: ')
grupo3 = input('Informe o terceiro grupo: ')
grupo4 = input('Informe o quarto grupo: ')

listarGrupos = [grupo1, grupo2, grupo3, grupo4]
shuffle(listarGrupos)
#print(listarGrupos)
print('A ordem de apresentação de grupos será:\n1ºGrupo: {} \n2ºGrupo: {} \n3ºGrupo: {} \n4ºGrupo: {}'.format(listarGrupos[0], listarGrupos[1], listarGrupos[2], listarGrupos[3]))
