#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velCarro = int(input('Informe a velocidade do carro: '))
if velCarro>80:
    print('Seu carro ultrapasou {}Km/h acima da velocidade permitida e será multado em R${:.2f}.'.format((velCarro-80), (velCarro-80)*7))
else:
    print('Seu carro está dentro do limite de velocidade permitido.')
print("Você não está no Velozes e Furiosos, respeite a velocidade permitida.")