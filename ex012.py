#12 Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valorProduto = float(input('Informe o valor do produto: '))
informarDesc = float(input('Informe o desconto a ser aplicado: '))
calculoDesc = valorProduto-(valorProduto*informarDesc/100)
print('Valor inicial do produto: R${}\n Valor de desconto aplicado: {}%\n Valor final do produto: R${:.2f}'.format(valorProduto, informarDesc,calculoDesc))

