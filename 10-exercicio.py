## F.U.P que peça um número e exiba a tabuada de 1 a 10 desse número.

num = int(input("Digite um número: "))
print("Tabuada do", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
