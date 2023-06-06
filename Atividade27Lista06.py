num = int(input("Informe um numero \n"))

i = 1
x = 1
h = 1
while i <= num:
    x = x * i
    h = h + (1/x)
    i = i + 1

print(h)