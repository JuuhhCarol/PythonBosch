import random
saldo = 100
print("Bem-vindo ao Jogo de Dados!🍀🎲")
print(f"Você começa com R${saldo}💰.\n")

while saldo > 0:
    try:
        aposta = int(input(f"Seu saldo: R${saldo}. Quanto deseja apostar? "))
        if aposta > saldo or aposta <= 0:
            print("Aposta inválida! Tente novamente.")  
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

    try:
        escolha = int(input("Tente adivinhar a soma de três dados (entre 3 e 18): "))
        if escolha < 3 or escolha > 18:
            print("Número inválido! Escolha um valor entre 3 e 18.")
        
    except ValueError:
        print("Entrada inválida! Digite um número inteiro entre 3 e 18.")
    

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dado3 = random.randint(1, 6)
    soma_dados = dado1 + dado2 + dado3

    print(f"\n🎲 Os dados rolaram: {dado1}, {dado2} e {dado3} (Soma = {soma_dados})")

    diferenca = abs(escolha - soma_dados)

    if escolha == soma_dados:
        ganho = aposta * 5
        saldo += ganho
        print(f"🎉 Parabéns! Você acertou e ganhou R${ganho}!🍀🍀🍀")
    else:
        saldo -= aposta
        print(f"❌ Que pena! Você perdeu R${aposta}.")

        if diferenca == 1 or diferenca == 2:
            print("🔥 Você quase acertou! Estava muito perto!")
        elif diferenca <= 5:
            print("🙂 Você estava perto! Tente de novo.")
        else:
            print("❄️ Você estava longe! Boa sorte na próxima.")
    if saldo > 0:
        continuar = input("\nDeseja jogar novamente? (s/n): ").lower()
        if continuar != 's':
            break

print(f"\nJogo encerrado. Seu saldo final é R${saldo}💰. Obrigado por jogar😉!")