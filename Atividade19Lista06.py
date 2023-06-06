"""
Escreva um algoritmo que leia um numero inteiro entre 100 e 999 e digite cada um dos algarismos
"""

Num = int(input("Informe um numero entre 100 e 999 para receber os algarismos separados \n"))

if Num > 999 or Num < 100:
    print("O numero informado é invalido")
else:
    Num = str(Num)
    Num = list(Num)
    print(f"Os algarismos dos numeros informados são de {Num[0]}, {Num[1]} e {Num[2]}")