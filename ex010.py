#10 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
#Considere US$:1.00 = BR$3.27
valorCarteira = float(input('Quanto você tem na carteira: BR$'))
valorDolar = float(5.467)
valorEuro = float(6.360)
valorIene = float(0.03492)
print('Dolar hoje: USD {:.2f}'.format(valorDolar))
print('Euro hoje: EUR {:.2f}'.format(valorEuro))
print('Iene hoje: JPY {:.2f}'.format(valorIene))
print('Sua carteira: BRL{:.2f}'.format(valorCarteira))
maxCompraDolar = valorCarteira / valorDolar
maxCompraEuro = valorCarteira / valorEuro
maxCompraIene = valorCarteira / valorIene
print('Valor máximo de compra (Dolar): USD {:.2f}'.format(maxCompraDolar))
print('Valor máximo de compra (Euro): EUR {:.2f}'.format(maxCompraEuro))
print('Valor máximo de compra (Iene): JPY {:.2f}'.format(maxCompraIene))

