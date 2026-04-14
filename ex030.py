#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

num = int(input('informe um número: '))
if num % 2 == 0:
    print('O número é PAR.')
else:
    print('O número é IMPAR.')
print('Fim da execução.')


#O resto da divisao de qualquer número par por 2 é 0.
#O resto da divisão de qualquer número impar por 2 é 1.