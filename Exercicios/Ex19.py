# Lista 

import random
def gerar(inferior,superior,tamanho):
    lista =[]
    for _ in range (tamanho):
        lista.append(random.randint(inferior,superior -1))
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                temporario = lista[i]
                lista[i] = lista[j]
                lista[j] = temporario 
    print(lista)
inferior=int(input("defina o minimo:"))
superior=int(input("defina o maximo:"))
tamanho=int(input("defina o tamanho:"))

gerar(inferior,superior,tamanho)