#Crie um programa que leia o nome completo der uma pessoa e mostre:
#O nome com todas as letras maiusculas.
#O nome com todas minusculas.
#Quantas letras ao todo (Sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = input('Digite o seu nome completo: ')
retirarEspacos = nome.replace(' ','')
dividirNome = nome.split()
print('Seu nome em maiusculo: {}'.format(nome.upper()))
print('Seu nome em minusculo: {}'.format(nome.lower()))
print('Seu nome possui {} letras no total.'.format(len(retirarEspacos)))
print('Seu primeiro nome tem {} letras.'.format((len(dividirNome[0]))))


#Resolição do Guanabara
#nome = str(input('Digite o seu nome completo: ')).strip() #Strip elminia os espacos no começo/fim da string
#print('Seu nome em maiusculo: {}'.format(nome.upper()))
#print('Seu nome em minusculo: {}'.format(nome.lower()))
#print('Seu nome possui {} letras no total.'.format(len(nome)-nome.count(' '))) #Vai contar quantos caracteres tem ao total com espaços com o len e depois subtrair os espaços com count
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' '))) #Vai indicar a posição do primeiro espaço sendo assim, como começa a contagem do 0 a posição que sair é a quantidade de letras da primeira palavra.
