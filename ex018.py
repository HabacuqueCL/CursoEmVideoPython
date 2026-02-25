#Faça um programa que leia um angulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse angulo
from math import sin, cos, tan, radians
valorAngulo = float(input('Informe o valor do Ângulo: '))
transAngulo = radians(valorAngulo)
sen = sin(transAngulo)
cos = cos(transAngulo)
tan = tan(transAngulo)
print('Os valores de Seno, Cosseno e Tangente de um angulo de {} são: Sen:{:.4f} Cos:{:.4f} Tang:{:.4f}'.format(valorAngulo, sen, cos, tan))

'''#RESOLUCAO GUANABARA
from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo que voce deseja: '))
seno = sin(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))'''
