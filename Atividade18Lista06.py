"""
Escreva um algoritmo que leia certa quantidade de numeros e informe quantas vezes o maior numero foi lido e qual foi
"""

vezes = int(input("Quantos numeros você deseja informar? \n"))

i = 0
Lista = []

while i < vezes:
    numero = int(input("Informe o numero que deseja adicionar \n"))
    i = i + 1
    Lista.append(numero)

print(f"O maior numero é de {max(Lista)} e a quantidade de vezes que apareceu foi de {Lista.count(max(Lista))}")