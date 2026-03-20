#Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente

nome = input('Insira o seu nome: ').strip()
splitNome = nome.split()
print('Primeiro nome: {}'.format(splitNome[0]))
print('Último nome: {}'.format(splitNome[-1]))

#Resolucao guanabara

#n = str(input('Digite seu nome completo: ')).strip()
#nome = n.split()
#print('Muito prazer em te conhecer!')
#print('Seu primeiro nome é: {}'.format(nome[0]))
#print('Seu último nome é: {}'.format(nome[len(nome)-1]))