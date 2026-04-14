from datetime import date

ano = int(input('informe a data: '))
if ano == 0:
    ano = date.today().year
    print(ano)
else:
    print('ano incorreto.')