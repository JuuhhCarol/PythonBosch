# Defina com quantos anos alguem pode votar 

ano = int(input("digite o ano que nasceu:"))
idade=(2025-ano)
if idade<=15:
    print("não pode votar")
elif idade>=16 or idade<=18:
    print("se quiser")
elif idade>=18 or idade<=70:
    print("pode votar!")
else:
    print("se quiser!")  