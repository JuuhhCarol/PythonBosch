#criando lista ordenada e com contagem

lista =[ ]
quantidade=int(input("oque deseja adicionar?"))
for i in range (quantidade):
    item=input(f"digite o item{i+1}:")
    lista.append(item)
lista.sort()
print("lista final:",lista)
print(len(lista))