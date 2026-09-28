##  F.U.P que gere um número aleatório de 1 a 100 e peça ao usuário para adivinhar, dando dicas de "maior" ou "menor" até acertar. 

import random
numero_secreto = random.randint(1, 100)
tentativas = 0
while True:
    palpite = int(input("Adivinhe o número (entre 1 e 100): "))
    tentativas += 1
    if palpite < numero_secreto:
        print("Tente um número maior.")
    elif palpite > numero_secreto:
        print("Tente um número menor.")
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
        break
    