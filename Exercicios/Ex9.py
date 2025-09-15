#Jogo par ou impar

import random
pontos=0
while True:
    print(pontos)
    escolha = input("você escolhe par ou impar?").strip().lower()
    numero_usuario = int(input ("digite um numero:"))
    numero_computador= random.randint(0,10)
    soma = numero_usuario+numero_computador
    resultado="par" if soma % 2== 0 else "impar"
    print (f"Você escolheu {numero_usuario},o computador escolheu {numero_computador}.A soma é {soma} e o resultado é {resultado} ")
    if resultado == escolha:
        print("parabéns você venceu!")
        pontos = 0+1
    else:
        print("o computador venceu!")
        break