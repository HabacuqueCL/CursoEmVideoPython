#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
from random import choice

nome1 = input('Informe o nome do primeiro aluno: ')
nome2 = input('Informe o nome do segundo aluno: ')
nome3 = input('Informe o nome do terceiro aluno: ')
nome4 = input('Informe o nome do quarto aluno: ')

nomesAlunos = [nome1, nome2, nome3, nome4]
sortearAluno = choice(nomesAlunos)
print('O aluno sorteado foi: {}'.format(sortearAluno))
