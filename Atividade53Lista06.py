Num = int(input("Digite um numero \n"))
i = 0
i2 = 0
i3 = 1
Sum = 2
Lista = []

for n in range(1, 10000):
    Lista.append(n)

while i < Num:
    print(Lista[i2:i3])
    i2 = i3
    i3 = i3 + Sum
    Sum = Sum + 1
    i = i + 1