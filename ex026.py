#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A";
#Em que posição ela aparece a primeira vez;
#Em que posição ela aparece a ultima vez.

frase = input('Digite uma frase: ').strip().upper()
print('A letra "A" aparece {}x na frase.'.format(frase.count('A')))
print('A letra "A" aparece a primeira vez na posição {} dentro da frase.'.format(frase.find('A')+1))
print('A letra "A" aparece a última vez na posição {} dentro da frase'.format(frase.rfind('A')+1))