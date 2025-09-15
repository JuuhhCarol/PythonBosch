#Baskhara 

import math
def bhaskara(a,b,c):
    delta = (b*b)-(4*a*c)
    if delta > 0 :
        raiz = math.sqrt(delta)
        x1=(-b + raiz)/(2 * a)
        x2=(-b - raiz)/(2 * a)
        print(x1, x2, "é o valor de x1 e x2")
        print("raizes da equação:",x1, x2)       
    else :
        print("não existem raizes reais!")
    
a= int(input("digite o valor de a:"))
b= int(input("digite o valor de b:"))
c= int(input("digite o valor de c:"))
bhaskara(a,b,c)