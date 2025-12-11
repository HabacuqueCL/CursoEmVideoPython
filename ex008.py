#08 Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
valor = float(input('Informe o valor em metros: '))
km = valor / 1000
hm = valor / 100
dam = valor / 10
dm = valor * 10
cm = valor * 100
mm = valor * 1000
print('Valor em metros: {}m \nQuilômetros: {}km  \nHectômetros: {}hm \nDecâmetro: {}dam \nDecímetro: {:.0f}dm \nCentímetros: {:.0f}cm \nMilímetros: {:.0f}mm '.format(valor, km, hm, dam, dm, cm, mm))

