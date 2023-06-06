"""
Faça um algoritmo que encontre o primeiro multiplo de 11, 13 ou 17 após um numero dado
"""

num = int(input("Insira um numero \n"))

i = 0
for n in range(num, num*20):
    if n % 11 == 0 or n % 13 == 0 or n % 17 == 0:
        i = i + 1
        print(n)
        if i == 1:
            break

