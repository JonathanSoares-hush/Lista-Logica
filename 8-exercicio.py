##F.U.P que informe a idade de uma pessoa e classifique-a comocriança (0-12), adolescente (13-17) ou adulto (18+). 

idade = int(input("Digite a idade da pessoa: "))
if idade >= 0 and idade <= 12:
    print("A pessoa é uma criança.")
elif idade >= 13 and idade <= 17:
    print("A pessoa é um adolescente.")
else:
    print("A pessoa é um adulto.")