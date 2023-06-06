"""
Faça um programa que receba dois numeros. Calcule e mostre:

* A soma dos numeros pares desse intervalo de numeros, incluindo os numeros digitados

* a multiplicação dos numeros impares desse intervalo, incluindo os digitados
"""

Numero1 = int(input("Informe o primeiro numero \n"))
Numero2 = int(input("Informe o segundo numero \n"))

Lista = []
Lista2 = []

if Numero1 > Numero2:
    for n in range(Numero2, Numero1 + 1):
        if n % 2 == 0:
            Lista.append(n)
else:
    for n in range (Numero1, Numero2 + 1):
        if n % 2 == 0:
            Lista.append(n)

print(f"A soma dos numeros pares deste intervalo, incluindo os numeros digitados é de {sum(Lista)}")

if Numero1 > Numero2:
    for m in range(Numero2, Numero1 + 1):
        if m % 2 != 0:
            Lista2.append(m)
else:
    for m in range(Numero1, Numero2 + 1):
        if m % 2 != 0:
            Lista2.append(m)

i = 0
Mult = 1

Numero3 = len(Lista2) + 1

for x in Lista2:
    Mult = Mult * x

print(f"A multiplicação dos numeros impares do intervalo, incluindo os digitados é igual a {Mult}")