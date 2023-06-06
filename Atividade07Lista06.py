"""
Crie um programa que leia 10 numeros inteiros positivos, ignorando os negativos, e após mostre a média
"""

i = 1
soma = 0
while i <= 10:
    numero = int(input(f"Informe o {i} numero a ser somado: "))

    if numero < 0:
        print("O numero informado é invalido")
    else:
        soma = numero + soma
        i = i + 1

print(soma/10)