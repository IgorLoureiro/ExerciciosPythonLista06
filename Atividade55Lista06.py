Num = int(input("Informe um numero inteiro não negativo: \n"))

Lista = []
i = 0
i2 = 2
i3 = 0

if Num < 0:
    print("Numero invalido, tente novamente")
else:
    while i < Num:
        i3 = 0
        for n in range(2, i2):
            if i2 % n == 0:
                i3 = i3 + 1
        if i3 == 0:
            Lista.append(i2)
            i = i + 1
        i2 = i2 + 1
print(Lista)