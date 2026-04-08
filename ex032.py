#Faca um programa que leia um ano qualquer e mostre se ele é bissexto.

from calendar import isleap
ano = int(input('Informe o ano: '))
verificaAno = isleap(ano)
if verificaAno==True:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
print('Fim de execução.')