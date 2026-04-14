#Faca um programa que leia um ano qualquer e mostre se ele é bissexto.

from calendar import isleap
ano = int(input('Informe o ano: '))
verificaAno = isleap(ano)
if verificaAno==True:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
print('Fim de execução.')

#Resolução Guanabara
#from datetime import date
#ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
#if ano == 0:
#    ano = date.today().year #Verifica e mostra o ano atual
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #Se o resto da divisão por 4 for diferente de 0 e o restante da divisão por 100 for diferente de 0 ou o resto da divisão por 400 for igual a 0.
#    print('O ano {} é BISSEXTO.'.format(ano))
#else:
#    print('O ano {} não é BISSEXTO.'.format(ano))