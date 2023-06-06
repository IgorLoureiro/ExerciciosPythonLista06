"""
Faça um programa que some todos os numeros naturais abaixo de 1000 que são multiplos de 3 e 5
"""

Lista = []

for n in range(3, 1001):
    if n % 3 == 0 or n % 5 == 0:
        Lista.append(n)

print(f"A soma de todos os numeros multiplos de 3 e 5 até 1000 é de {sum(Lista)}")