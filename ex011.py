#11 Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
print('Informe a altura e a largura da parede em metros.')
valorAltura = float(input('Altura: '))
valorLargura = float(input('Largura: '))
valorArea = valorAltura * valorLargura
rendTinta = 2.0
tintaNecessária = (valorArea/rendTinta/1)*1 #Levando em conta 1 demão de tinta
print('Área da sua parede: {}m²'.format(valorArea))
print('A quantidade de tinta necessária para pintar {}m² é: {} litros '.format(valorArea, tintaNecessária))

