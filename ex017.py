#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
# <Cateto Oposto \/Cateto Adjacente /\Hipotenusa 
from math import exp, sqrt
catetoOposto = float(input('Informe o valor do Cateto Oposto: '))
catetoAdjacente = float(input('Informe o valor do Cateto Adjacente: '))
calculoCatetos = (pow(catetoOposto, 2))+(pow(catetoAdjacente, 2))
raizCalculoCatetos = sqrt(calculoCatetos)
print('A hipotenusa de um triângulo retângulo cujo o cateto oposto ({}) e cateto adjacente ({}) é de {:.2f}.'.format(catetoOposto, catetoAdjacente, raizCalculoCatetos))
#print(potCatetoOposto,potCatetoAdjacente,somaCatetos,raizSomaCatetos)


'''#RESOLUÇÃO GUANABARA
co = float(input('informe o co:'))
ca = float(input('informe o ca:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('a hi é {:.2f}'.format(hi))'''

'''from math import hypot
co = float(input('Comprimento do co:'))
ca = float(input('Comprimento do ca:'))
hi = hypot(co, ca)
print('A hi vai medir: {:.2f}'.format(hi))'''