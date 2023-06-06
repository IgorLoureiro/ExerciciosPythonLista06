"""
Faça um programa que leia um numero inteiro N e depois imprime N numeros impares após o numero N digitado
"""
Lista = []
i = 0
Numero = int(input("Escreva um numero para receber seus próximos valores impares: "))

for n in range(Numero+1, Numero + (Numero*3)):
    if n % 2 != 0:
        Lista.append(n)
        i = i + 1
        if i == Numero:
            break

print(f"Os próximos {Numero} numeros impares apartir de {Numero} são {Lista}")
