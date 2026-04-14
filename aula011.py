#Mudando a cor no terminal.
#Exemplo colocando o padrão de cor ANSI direto dentro da string.
n1 = 3
n2 = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m !!!'.format(3, 5))

#Exemplo colocando o padrão de cor ANSI dentro do .format
nome = 'Habacuque'
print('Olá, muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;32m',nome,'\033[m'))

#Exemplo utilizando lista em uma variavel
nome = 'Habacuque'
cores = {'limpa':'\033[m', 
         'azul':'\033[34m', 
         'amarelo':'\033[33m', 
         'pretoebranco':'\033[7;30m'}
print('Olá, muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
