#Faça um programa que leia um angulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse angulo
from math import sin, cos, tan, radians
valorAngulo = int(input('Informe o valor do Ângulo: '))
transAngulo = radians(valorAngulo)
sen = sin(transAngulo)
cos = cos(transAngulo)
tan = tan(transAngulo)
print('Os valores de Seno, Cosseno e Tangente de um angulo de {} são: Sen:{:.4f} Cos:{:.4f} Tang:{:.4f}'.format(valorAngulo, sen, cos, tan))
