#13 Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento.

valSalario = float(input('Informe salário: '))
valAdicional = float(input('Informe % à adicionar: '))
calcAumento = valSalario+(valSalario*valAdicional/100)
print('Salário informado: R${:.2f}\n Porcentagem de aumento: {}%\n Salário final: {:.2f}'.format(valSalario,valAdicional,calcAumento))

