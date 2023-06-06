Num1 = int(input("Informe dois numeros para receber todos os numeros primos entre eles: \n"))
Num2 = int(input())

Lista2 = []
i3 = 0

if Num1 > Num2:
    i3 = Num2
    if Num2 == 1:
        Num2 = 2
        i3 = Num2
    while i3 < Num1:
        i2 = 0
        for n in range(Num2, Num1 + 1):
            if i3 % n == 0 and i3 != n:
                i2 = i2 + 1
        if i2 == 0:
            Lista2. append(i3)
        i3 = i3 + 1
else:
    i3 = Num1
    if Num1 == 1:
        Num1 = 2
        i3 = Num1
    while i3 < Num2:
        i2 = 0
        for n in range(Num1, Num2 + 1):
            if i3 % n == 0 and i3 != n:
                i2 = i2 + 1
        if i2 == 0:
            Lista2.append(i3)
        i3 = i3 + 1

if len(Lista2) == 0:
    print("Não há numeros primos neste intervalo")
else:
    print(f"Existem {len(Lista2)} numeros primos neste intervalo, sendo eles respectivamente {Lista2}")

