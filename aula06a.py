n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
#print('A soma vale',soma) <-- Funciona mas é uma forma antiga de formatar o texto.
print('A soma entre {} e {} vale {}.'.format(n1, n2, soma))