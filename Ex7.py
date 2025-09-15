#Tabuleiro

def criar_tabuleiro(tamanho):
    for i in range (tamanho):
        for j in range(tamanho):
            print("X", end=" ")
        print(" ")
tamanho= int(input("digite o tamanho do tabuleiro:"))
criar_tabuleiro(tamanho)