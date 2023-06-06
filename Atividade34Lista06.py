"""
Faça um programa que calcule o menor numero divisivel por cada um dos numeros de 1 a 10
"""

i = 1
divisores = 0

while divisores != 10:
    for n in range(1, 12):
        if i % n == 0 and n < 11:
            divisores = divisores + 1
            if divisores == 10:
                break
        elif n == 11:
            i = i + 1
            divisores = 0

print(i)