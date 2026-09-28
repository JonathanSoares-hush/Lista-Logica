## F.U.P que peça um número e faça uma contagem regressiva até zero.

num = int(input("Digite um número: "))
if num < 0:
    print("Por favor, digite um número não negativo.")
else:
    for i in range(num, -1, -1):
        print(i)