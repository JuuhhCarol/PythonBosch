#crie um programa que o usuário escolhe uma palavra e o programa diz quantas vezes essa palavra aparece

palavra=(input('digite uma palavra:'))
arquivo= open('arquivo.txt','r')
letras=0
leitura= arquivo.read()
lista= leitura.split()
for i in lista:
    if palavra == i:
        letras += 1
print(letras)