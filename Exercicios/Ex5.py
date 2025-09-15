#criando um lista de somas

num = int(input("digite um numero"))
soma = 0
i = 1
while i <= num:
    soma += i 
    i += 1
print(f"a soma de 1 ate {num}é :{soma}")