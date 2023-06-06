"""
Escreva um programa para cálcular o valor da série, para 5 termos

S = 0+1/2!+2/4!+3/6!+4/8!+5/10!
"""
S = 0
num = 1
i = 1


while i <= 5:
    num = num * i
    S = S + (i / num)
    i = i + 1

print(S)
