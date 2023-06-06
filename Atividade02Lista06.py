"""
Escreva um programa que escreva na tela de 1 até 100, de 1 em 1, 3 vezes. A primeira vez deve usar for, a segunda while
e a terceira do while
"""

for n in range (1, 101):
    print(f"{n}")

x = 0
while x < 100:
    x = x + 1
    print(x)

z = 0
while True:
    z = z + 1
    print(z)
    if not z < 100:
        break