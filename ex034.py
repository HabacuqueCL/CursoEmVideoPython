#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00 calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

informeSalario = int(input('Informe o seu salário: '))
if informeSalario > 1250:
    print('O seu salário teve um aumento de 10% totalizando {}.'.format(informeSalario + (informeSalario*10/100)))
if informeSalario <= 1250:
    print('O seu salário teve um aumento de 15%. O valor ajustado é de {}.'.format(informeSalario + (informeSalario*15/100)))