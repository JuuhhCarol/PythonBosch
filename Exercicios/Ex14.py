#Uso de excessão

def imprima_ordenado(colecao):
    try:
        colecao.sort()
    except AttributeError:
        print("imutavel")
        pass
    print(colecao,"\n")
    

imprima_ordenado([3,2,1])
imprima_ordenado((3,2,1))
imprima_ordenado("321")