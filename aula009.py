#FATIANDO CARACTERES

frase = 'Curso em Vídeo Python'
print(frase[9]) #Vai mostrar o caractere que estiver na posição 9. Saida: V
print(frase[9:21]) #Vai mostrar do caractere 9 até o penultimo. Saida: Vídeo Python
print(frase[9:21:2]) #Vai mostrar a partir do caractere 9 até o penultimo pulando de 2 em dois. Saida: VdoPto 
print(frase[:5]) #Não colocar o primeiro caractere em que comeca vai fazer com que ele comece do primeiro e vá até o penultimo caractere do que foi indicado. Saida: Curso
print(frase[15:]) #Não colocar o caractere final vai fazer com que ele comece do caractere 15 e vá até o final da cadeia de caracteres. Saida: Python
print(frase[9::3]) #O 9 indica em qual caractere eu quero comecar, o que está em branco indica que eu quero que vá até o final da string e o 3 indica que eu quero pular de 3 em 3 caracteres. Saida: VePh

#ANALISE DE CARACTERES

print(len(frase)) #Quantos caracteres tem nessa string
print(frase.count('o')) #Conta quantas letras "o" menuscula aparece na string. Lembrando que é case sensitive (Um 'O' maiusculo ele não contaria)