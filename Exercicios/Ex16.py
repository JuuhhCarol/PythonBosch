#Soma de numeros aprimorada 

while True:
    try:
        numeros=int(input("digite um numero maior que zero:"))
        if numeros>0:
            lista=[int(digito) for digito in str(numeros)]
            soma=sum(lista)
            print(f'a soma dos algarismos de {numeros} é {soma}')
            break
        else:
            print('tente um numero maior:')
    except ValueError:
        print("entrada invalida,digite um NUMERO!")