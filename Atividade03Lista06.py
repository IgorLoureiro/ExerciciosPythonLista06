"""
Faça um programa que mostre uma contagem regressiva na tela de 10 a 0 e após mostrar a mensagem "FIM!"
"""

n = 11
while n > 0:
    n = n - 1
    print(n)
    if n == 0:
        print("Fim!")