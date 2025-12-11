#Exercicio extra
# Faça um algoritmo que laia o valor de um produto e mostre na tela quanto vai ficar esse valor com um desconto de 10% para pagamento a vista e 8% de aumento no valor para pagamento parcelado.
valorProduto = float(input('Informe o valor do produto: '))
calcAVista = valorProduto-(valorProduto*10/100)
calcParcelado = valorProduto+(valorProduto*8/100)

print('O valor do produto à vista com desconto de 10%'+' fica: R${}'.format(calcAVista))
print('O valor do produto parcelado com aumento de 8%'+' fica: R${}'.format(calcParcelado))
print('1x de R${:.2f}\n2x de R${:.2f}\n3x de R${:.2f}\n4x de R${:.2f}\n5x de R${:.2f}\n6x de R${:.2f}\n7x de R${:.2f}\n8x de R${:.2f}\n9x de R${:.2f}\n10x de R${:.2f}\n11x de R${:.2f}\n12x de R${:.2f}'.format(calcParcelado/1, calcParcelado/2, calcParcelado/3, calcParcelado/4, calcParcelado/5, calcParcelado/6, calcParcelado/7, calcParcelado/8, calcParcelado/9, calcParcelado/10, calcParcelado/11, calcParcelado/12))

