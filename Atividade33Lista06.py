Num1 = int(input("Digite a quantidade de numeros após os numeros digitados para verificar seus multiplos \n"))
Num2 = int(input("Digite um numero \n"))
Num3 = int(input("Digite o segundo numero \n"))

i = 0
Numeros = []
Numeros.append(Num2)
Numeros.append(Num3)
Numeros.sort()
Lista = []

for n in range(Numeros[0], (Numeros[1]*10)):
     if n % Num2 == 0 or n % Num3 == 0:
        i = i + 1
        Lista.append(n)
        if i == Num1:
            break


print(f"Os multiplos de {Num2} e {Num3} são {Lista}")