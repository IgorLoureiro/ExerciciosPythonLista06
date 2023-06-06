"""
faça um programa que mostre os 5 primeiros multiplos de 3, considerando apartir do numero 1
"""

i = 0

for n in range(1, 50):
    if n % 3 == 0:
        i = i + 1
        print(f"{n}")
        if i == 5:
            break