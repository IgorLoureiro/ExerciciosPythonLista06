"""
Faça um programa que leia um numero inteiro positivo N e imprima todos os numeros naturais até N
"""

Numero = int(input("Digite um numero inteiro para receber todos os numeros antes deste \n"))
Lista = []
if Numero > 0:
    for n in range(1, Numero+1):
        Lista.append(n)
        if n == Numero:
            print(Lista)
else:
    print("Numero invalido, por favor, digite um numero positivo")


