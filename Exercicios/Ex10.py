#Numeros primos 

divisores=[]
num = int(input("digite um numero:"))
for i in range(1, num+1):
    if num % i == 0: 
        divisores.append(i)
if len (divisores) ==2:
    print(f"{num} é primo")
else:
    print(f"{num} não é primo!")
print(divisores) 