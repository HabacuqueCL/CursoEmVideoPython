import random
print('O sistema está escolhendo um número...')
num = random.randint(1,5)
escolheNum = int(input('Adivinhe o número que o sistema escolheu: '))
if num == escolheNum:
    print('Número gerado pelo sistema: {}'.format(num))
    print('Número escolhido pelo usuário: {}'.format(escolheNum))
    print('Parabéns você acertou!')
else:
    print('Número gerado pelo sistema: {}'.format(num))
    print('Número escolhido pelo usuário: {}'.format(escolheNum))
    print('Que Pena! Tente novamente.')
print('Fim da execução.')