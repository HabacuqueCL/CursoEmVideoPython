#FATIANDO CARACTERES

frase = 'Curso em Vídeo Python'
print(frase[9]) #Vai mostrar o caractere que estiver na posição 9. Saida: V
print(frase[9:21]) #Vai mostrar do caractere 9 até o penultimo. Saida: Vídeo Python
print(frase[9:21:2]) #Vai mostrar a partir do caractere 9 até o penultimo pulando de 2 em dois. Saida: VdoPto 
print(frase[:5]) #Não colocar o primeiro caractere em que comeca vai fazer com que ele comece do primeiro e vá até o penultimo caractere do que foi indicado. Saida: Curso
print(frase[15:]) #Não colocar o caractere final vai fazer com que ele comece do caractere 15 e vá até o final da cadeia de caracteres. Saida: Python
print(frase[9::3]) #O 9 indica em qual caractere eu quero comecar, o que está em branco indica que eu quero que vá até o final da string e o 3 indica que eu quero pular de 3 em 3 caracteres. Saida: VePh

print(frase)

#ANALISE DE CARACTERES

print(len(frase)) #Quantos caracteres tem nessa string
print(frase.count('o')) #Conta quantas letras "o" menusculas aparecem na string. Lembrando que é case sensitive (Um 'O' maiusculo ele não contaria)
print(frase.count('o',0,13)) #Verifica quantos caracteres "o" existe entre a posição 0 á posição 13 Saída: 1
print(frase.find('deo')) #Vai mostrar a posição em que começa o "deo" ou seja na posição 11
print(frase.find('Android')) #Em casos que ele não encontra a string informada dentro da string da variável ele vai informar a posição -1
print('Curso' in frase) #Verifica se a frase "Curso" existe na string e retorna true se existir ou false se não existir diferente do find que informa a posição da string na frase.

#TRANSFORMAÇÃO DE CARACTERES

print(frase.replace('Python','Android')) #Vai substituir a string Python por Android na string
print(frase.upper()) #Deixa todos os caracteres da string em maiusculo exceto as que já estão em maiusculo Saida: CURSO EM VÍDEO PYTHON
print(frase.lower()) #Deixa todos os caracteres em menusculo exceto as que já estão em menusculo Saida: curso em vídeo python
print(frase.capitalize()) #Tranforma toda a string em menusculo e deixa só o primeiro caractere em maiusculo Saida: Curso em vídeo python
print(frase.title()) #Vai verificar quantas palavras que tem na string e vai colocar cada uma delas com a primeira letra em maiusculo Saida: Curso Em Vídeo Python

frase1 = '   Aprenda Python  '
print(frase1)
print(frase1.strip()) #Remove todos os espaços inuteis no começo e no final da string
print(frase1.lstrip()) #Remove todos os espaços inuteis do lado esquerdo da string
print(frase1.rstrip()) #Remove todos os espaços inuteis do lado direito da string

#DIVISAO DE STRINGS

print(frase.split()) #Gera uma lista de todas as plavras dentro de uma cadeira de caracteres Saida: ['Curso', 'em', 'Vídeo', 'Python']

#JUNCAO DE STRINGS

print('-'.join(frase)) #Coloca o traço entre cada letra de caractere de uma string
print('-'.join(frase.split())) #O join nesse exemplo junta as palavras que foram separadas com split com o traço, no caso de só adicionar um espaco coloque as aspas com um espaço dentro delas ' '.

print("""Aqui o aluno terá um material organizado em parágrafos curtos e diálogos claros, facilitando o aprendizado desde o início. Os elementos principais da língua serão ensinados, tais como a parte gramatical e de vocabulário.""")   