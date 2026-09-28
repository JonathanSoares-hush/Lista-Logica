## F.U.P que peça o valor de uma compra e aplique um desconto de 10% se for acima de R$ 100,00.

valor_compra = float(input("Digite o valor da compra: "))
if valor_compra > 100:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print("O valor final com desconto é: R$", valor_final)
else:
    print("O valor da compra não é elegível para desconto.")
