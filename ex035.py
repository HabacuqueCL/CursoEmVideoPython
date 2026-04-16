#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem formar um triângulo ou não.

n1 = float(input('Valor 1: '))
n2 = float(input('Valor 2: '))
n3 = float(input('Valor 3: '))
maiorNum = max(n1,n2,n3)
if (n1+n2+n3)-maiorNum>maiorNum:
    print('É um triângulo.')
else:
    print('Não é um triângulo.')


#Resolução Guanabara
#r1 = float(input('Primeiro segmento: '))
#r2 = float(input('Segundo segmento: '))
#r3 = float(input('Terceiro segmento: '))
#if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#    print('Os segmentos PODEM FORMAR UM TRIANGULO.')
#else:
#    print('Os segmentos NÃO PODEM FORMAR UM TRIANGULO.')

#Cálculo: O 1º segmento tem que ser menor que os outros dois segmentos. o 2º segmento tem que ser menor que os outros dois e o 3º segmento tem que ser menor que os outros dois segmentos. Todos eles sendo true, formam um triangulo, do contrário, não formam.