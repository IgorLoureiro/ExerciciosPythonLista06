"""
Faça um algoritmo que leia um numero positivo e imprima seus divisores
"""

Numero = int(input("Informe um numero positivo para receber seus divisores \n"))
Lista = []

if Numero > 0:
    for n in range(1, Numero + 1):
        if Numero % n == 0:
            Lista.append(n)
    print(f"Os divisores do numero informado são de {Lista} ")
else:
    print("Numero invalido")

