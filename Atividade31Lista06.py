i = 1
S = 0
n = 0
while i < 99 and n < 51:
    for n in range(1, 51):
        S = S + (i/n)
        i = i + 2

print(S)