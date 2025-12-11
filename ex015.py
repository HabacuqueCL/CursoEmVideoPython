#15 Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

diasAlugados = float(input('Informe por quantos dias o carro foi alugado: '))
distanciaPercorrida = float(input('Informe a distância percorrida em kilometros(Km): '))
calculoAluguel = (diasAlugados*60.0)+(distanciaPercorrida*0.15)
print('O aluguel do seu carro ficou R${:.2f}'.format(calculoAluguel))