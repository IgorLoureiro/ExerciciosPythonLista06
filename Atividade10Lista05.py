"""
Faça um programa que calcule e mostre a soma dos 50 primeiros numeros pares
"""

i = 0
soma = 0

for n in range(1, 101):
    if n % 2 == 0:
        i = i + 1
        soma = soma + n
        if i == 50:
            break

print(f"A soma total é de {soma}")
