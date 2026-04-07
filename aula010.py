#idadeCarro = int(input('Quantos anos têm o seu carro? '))
#if idadeCarro<=3:
#    print('Seu carro é novo!')
#else:
#    print('Seu carro é velho!')
#print('Fim da execução.')

primeiraNota = float(input('Informe a primeira nota: '))
segundaNota = float(input('Informe a segunda nota: '))
media = (primeiraNota+segundaNota)/2
print('A sua média foi {}.'.format(media))
if media>=6:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua média foi ruim, melhore!')
print('Fim da execução.')