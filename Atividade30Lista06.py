num = int(input("Digite um numero \n"))
print(f"O calculo sera feito até {(2*num) - 1}")

i = 1
calc = 0
sinal = 1
while i < (2*num) - 1:
    calc = calc + (sinal*i)
    i = i + 1
    sinal = -sinal

print(calc)

