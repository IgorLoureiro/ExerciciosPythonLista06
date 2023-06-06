"""
Leia uma sequencia de numeros inteiros e determine se eles são pares ou não, devera ser mostrado o numero de
numeros lidos e quantidade de numeros pares, o processo deve terminar quando for digitado o numero 1000
"""

Numero = int(input("Informe um numero para saber se ele é par, para finalizar, digite o numero 1000 \n"))

i = 0
x = 0

while Numero != 1000:
    if Numero % 2 == 0:
        i = i + 1
        x = x + 1
        print("O numero é par")
        Numero = int(input("Informe um numero para saber se ele é par, para finalizar, digite o numero 1000 \n"))
    else:
        i = i + 1
        print("O numero é impar")
        Numero = int(input("Informe um numero para saber se ele é par, para finalizar, digite o numero 1000 \n"))

print(f"A quantidade de numeros inforamdos foi de {i} e a quantidade de Numeros pares foi {x}")