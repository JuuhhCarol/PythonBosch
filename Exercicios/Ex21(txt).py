#Uso de txt em py

with open ('matriculas.txt','w') as arquivo:
    alunos=0
    while True:
        matricular=(input("deseja realizar uma matricula? \n s - SIM \n n - não"))
        if matricular=='s':
            alunos+=1
            arquivo.write(input("digite o nome do aluno:"))
            arquivo.write(',')
            arquivo.write(input("digite o nome do curso:"))
            arquivo.write(',')
            arquivo.write(input("digite a matricula:"))
            arquivo.write('\n')
        else:
            print(f"a quantidade de alunos é:{alunos}")
            break