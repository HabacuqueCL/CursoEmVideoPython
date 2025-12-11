#06 Crie um algoritmo que leia um algoritmo e mostre o seu dobro, triplo e raiz quadrada.
valor = int(input('Informe um número: '))
dobro = valor*2
triplo = valor*3
raizQuadrada = valor**(1/2)
print('O dobro de {} é: {}'.format(valor, dobro))
print('O trplo de {} é: {}'.format(valor, triplo))
print('A raiz quadrada de {} é: {:.2f}'.format(valor, raizQuadrada))