#05 Crie um programa que leia um número inteiro e mostre na tela o seu sucessor seu antecessor.
#valor = int(input('Digite um número: '))
#sucessor = valor - 1
#antecessor = valor + 1
#print('Valor informado: {}\n Sucessor: {}\n Antecessor: {}'.format(valor, sucessor, antecessor))

#06 Crie um algoritmo que leia um algoritmo e mostre o seu dobro, triplo e raiz quadrada.
#valor = int(input('Informe um número: '))
#dobro = valor*2
#triplo = valor*3
#raizQuadrada = valor**(1/2)
#print('O dobro de {} é: {}'.format(valor, dobro))
#print('O trplo de {} é: {}'.format(valor, triplo))
#print('A raiz quadrada de {} é: {:.2f}'.format(valor, raizQuadrada))

#07 Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
#nota1 = float(input('Digite a primeira nota: '))
#nota2 = float(input('Digite a segunda nota: '))
#media = (nota1+nota2)/2
#print('A média das notas {} e {} é: {:.5f}'.format(nota1,nota2,media))

#08 Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
#valor = float(input('Informe o valor em metros: '))
#km = valor / 1000
#hm = valor / 100
#dam = valor / 10
#dm = valor * 10
#cm = valor * 100
#mm = valor * 1000
#print('Valor em metros: {}m \nQuilômetros: {}km  \nHectômetros: {}hm \nDecâmetro: {}dam \nDecímetro: {:.0f}dm \nCentímetros: {:.0f}cm \nMilímetros: {:.0f}mm '.format(valor, km, hm, dam, dm, cm, mm))

#09 Faça um programa de leia um número inteiro qualquer e mostre na tela a sua tabuada.
#valor = int(input('Insira um valor: '))
#mult1 = valor * 1
#mult2 = valor * 2
#mult3 = valor * 3
#mult4 = valor * 4
#mult5 = valor * 5
#mult6 = valor * 6
#mult7 = valor * 7
#mult8 = valor * 8
#mult9 = valor * 9

#print('#'+('-'*21)+'#')
#print('| A tabuada do {} é: \n| {}x1 = {}  \n| {}x2 = {}  \n| {}x3 = {} \n| {}x4 = {} \n| {}x5 = {} \n| {}x6 = {} \n| {}x7 = {} \n| {}x8 = {}  \n| {}x9 = {}'.format(valor,valor,mult1,valor,mult2,valor,mult3,valor,mult4,valor,mult5,valor,mult6,valor,mult7,valor,mult8,valor,mult9))
#print('#'+('-'*21)+'#')

#10 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
#Considere US$:1.00 = BR$3.27
#valorCarteira = float(input('Quanto você tem na carteira: BR$'))
#valorDolar = float(5.467)
#valorEuro = float(6.360)
#valorIene = float(0.03492)
#print('Dolar hoje: USD {:.2f}'.format(valorDolar))
#print('Euro hoje: EUR {:.2f}'.format(valorEuro))
#print('Iene hoje: JPY {:.2f}'.format(valorIene))
#print('Sua carteira: BRL{:.2f}'.format(valorCarteira))
#maxCompraDolar = valorCarteira / valorDolar
#maxCompraEuro = valorCarteira / valorEuro
#maxCompraIene = valorCarteira / valorIene
#print('Valor máximo de compra (Dolar): USD {:.2f}'.format(maxCompraDolar))
#print('Valor máximo de compra (Euro): EUR {:.2f}'.format(maxCompraEuro))
#print('Valor máximo de compra (Iene): JPY {:.2f}'.format(maxCompraIene))

#11 Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
#print('Informe a altura e a largura da parede em metros.')
#valorAltura = float(input('Altura: '))
#valorLargura = float(input('Largura: '))
#valorArea = valorAltura * valorLargura
#rendTinta = 2.0
#tintaNecessária = (valorArea/rendTinta/1)*1 #Levando em conta 1 demão de tinta
#print('Área da sua parede: {}m²'.format(valorArea))
#print('A quantidade de tinta necessária para pintar {}m² é: {} litros '.format(valorArea, tintaNecessária))

#12 Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valorProduto = float(input('Informe o valor do produto: '))
informarDesc = float(input('Informe o desconto a ser aplicado: '))
calculoDesc = valorProduto-(valorProduto*informarDesc/100)
print('Valor inicial do produto: R${}\n Valor de desconto aplicado: {}%\n Valor final do produto: R${:.2f}'.format(valorProduto, informarDesc,calculoDesc))

#13 Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento.

#valSalario = int(input('Informe salário: '))
#valAdicional = int(input('Informe % à adicionar: '))
#calcAumento = (valSalario/100)*valAdicional+valSalario
#print('Salário informado: R${}\n Porcentagem de aumento: {}\n Salário final: {}'.format(valSalario,valAdicional,calcAumento))

