"""
Escreva um programa que leia 10 numeros e imprima o menor e o maior deles
"""
Lista = []
for n in range(1, 11):
    numero = int(input("Digite um numero: "))
    Lista.append(numero)

print(f"Dos numeros digitados o maior é {max(Lista)} e o menor é {min(Lista)}")
