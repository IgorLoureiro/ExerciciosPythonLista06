Saque = int(input("Informe o valor que deseja sacar"))
i100 = 0
i50 = 0
i20 = 0
i10 = 0
i5 = 0
i2 = 0
i1 = 0
while Saque > 0:
    if Saque >= 100:
        while Saque >= 100:
            Saque = Saque - 100
            i100 = i100 + 1
        print(f"Serão necessárias {i100} notas de cem")
    if Saque >= 50:
        while Saque >= 50:
            Saque = Saque - 50
            i50 = i50 + 1
        print(f"Serão necessárias {i50} notas de cinquenta")
    if Saque >= 20:
        while Saque >= 20:
            Saque = Saque - 20
            i20 = i20 + 1
        print(f"Serão necessárias {i20} notas de vinte")
    if Saque >= 10:
        while Saque >= 10:
            Saque = Saque - 10
            i10 = i10 + 1
        print(f"Serão necessárias {i10} notas de 10")
    if Saque >= 5:
        while Saque >= 5:
            Saque = Saque - 5
            i5 = i5 + 1
        print(f"Serão necessárias {i5} notas de cinco")
    if Saque >= 2:
        while Saque >= 2:
            Saque = Saque - 2
            i2 = i2 + 1
        print(f"Serão necessárias {i2} notas de dois")
    if Saque >= 1:
        while Saque >= 1:
            Saque = Saque - 1
            i1 = i1 + 1
        print(f"Serão necessárias {i1} notas de um")