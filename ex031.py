#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem. Cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distViagem = int(input('Informe a distância em KMs da viagem: '))
if distViagem<=200:
    print('Sua viagem foi de até 200Km, será cobrado R$0,50 por Km rodado totalizando R${:.2f}'.format(float(distViagem*0.50)))
else:
    print('Sua viagem foi maior que 200Km, será cobrado R$0,45 por Km rodado totalizando R${:.2f}'.format(float(distViagem*0.45)))
print('Fim da execução.')