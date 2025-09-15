# Escreve datas em extenso 

meses ={
        "janeiro": "01","fevereiro":"02","março":"03","abril":"04","maio":"05","junho":"06","julho":"07","agosto":"08","setembro":"09","outubro":"10","novembro":"11", "dezembro":"12"
}
extenso=(input("Digite a data de hoje:"))
minusculas= extenso.lower()
cotoco=[]
cotoco=minusculas.split(' de ')
print(f"{cotoco[0]}/{meses[cotoco[1]]}/{cotoco[2]}")