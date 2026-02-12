#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
# <Cateto Oposto \/Cateto Adjacente /\Hipotenusa 
from math import exp, sqrt
catetoOposto = int(input('Informe o valor do Cateto Oposto: '))
catetoAdjacente = int(input('Informe o valor do Cateto Adjacente: '))
calculoCatetos = (pow(catetoOposto, 2))+(pow(catetoAdjacente, 2))
raizCalculoCatetos = sqrt(calculoCatetos)
print('A hipotenusa de um triângulo retângulo cujo o cateto oposto ({}) e cateto adjacente ({}) é de {:.0f}.'.format(catetoOposto, catetoAdjacente, raizCalculoCatetos))
#print(potCatetoOposto,potCatetoAdjacente,somaCatetos,raizSomaCatetos)