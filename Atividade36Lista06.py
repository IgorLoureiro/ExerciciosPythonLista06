Lista = []

Num = 0
for n in range(1, 101):
    Num = Num + (n**2)
    Lista.append(Num)

print(Lista)
Soma = sum(Lista)
Quadrado = Soma**2

print(Soma)

Result = Quadrado - Soma

print(Result)