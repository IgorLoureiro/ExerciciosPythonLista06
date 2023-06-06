"""
Faça um programa que solicite ao usuario 10 numeros e some-os
"""

i = 1
soma = 0
while i <= 10:
    numero = int(input(f"Informe o {i} numero a ser somado: "))
    soma = numero + soma
    i = i + 1

print(soma)