"""
Faça um programa que leia um numero inteiro positivo n e calcule a soma dos n primeiros numeros naturais
"""

Numero = int(input("Escreva um numero natural para receber os numeros naturais somados \n"))

soma = 0

if Numero > 0:
    for n in range(1, Numero+1):
        soma = soma + n
    print(soma)
else:
    print("O numero informado não é natural")
