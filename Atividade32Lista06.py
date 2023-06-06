from random import randint

V = int(input("Quantas vezes você deseja jogar os dados? \n"))

i = 0

while i < V:
    i = i + 1
    Dado1 = randint(0, 6)
    Dado2 = randint(0, 6)
    if Dado1 == Dado2:
        print(f"O valor dos dados foram {Dado1} e {Dado2}")
        print("Os valores são idênticos")
    elif Dado1 > Dado2:
        print(f"O valor dos dados foram {Dado1} e {Dado2}")
        print(f"O valor {Dado1} é maior que o valor {Dado2}")
    elif Dado2 > Dado1:
        print(f"O valor dos dados foram {Dado1} e {Dado2}")
        print(f"O valor {Dado2} é maior que o valor {Dado1}")




