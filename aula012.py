nome = str(input('Qual o seu nome? '))
if nome == 'Habacuque':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem comum no Brasil.')
elif nome in 'Anna Claudia Luciana Joelma':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem comum.')
print('Tenha um bom dia, {}!'.format(nome))

#Obs¹: Voce pode usar um IF, vários ELIFs e um ELSE. Voce também pode ter um IF, vários ELIFs e nenhum ELSE.