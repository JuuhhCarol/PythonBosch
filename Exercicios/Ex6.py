#calculadora

while True:
    numum = int (input("digite o primeiro numero:"))
    numdois = int (input("digite o segundo numero:"))
    operacao = int(input("qual operação que deseja fazer?\n[1]:soma\n[2]subtracao:\n[3]:multiplicacao\n[4]:divisao \n[0]:sair")) 
    if operacao ==0:
        break
    elif operacao == 1:
        resultado = (numum+numdois)
        print(f"{numum}+{numdois}={resultado}")
    elif operacao == 2:
        resultado = (numum-numdois)
        print(f"{numum}-{numdois}={resultado}")
    elif operacao == 3:
        resultado = (numum*numdois)
        print(f"{numum}{numdois}={resultado}")
    elif operacao == 4:
        resultado = (numum/numdois)
        print(f"{numum}/{numdois}={resultado}")