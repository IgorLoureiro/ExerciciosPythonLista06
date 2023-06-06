Num1 = int(input("Informe um numero para realizar uma operação de sua escolha: \n"))
Num2 = int(input("Informe um segundo numero para realizar uma operação de sua escolha: \n"))
NumSelect = int(input("Selecione a opção desejada: \n 1 - Adição \n 2- Subtração \n 3 - Multiplicação "
                      "\n 4 - Divisão \n 5 - Sair \n"))

match NumSelect:
    case 1:
        Num3 = Num1 + Num2
        print(f"A soma de {Num1} + {Num2} é igual a {Num3}")
    case 2:
        Num3 = Num1 - Num2
        print(f"A subtração de {Num1} - {Num2} é igual a {Num3}")
    case 3:
        Num3 = Num1 * Num2
        print(f"A multiplicação de {Num1} vezes {Num2} é igual a {Num3}")
    case 4:
        Num3 = Num1/Num2
        print(f"A divisão de de {Num1} por {Num2} é igual a {Num3}")
    case 5:
        print("Tchau")
    case _:
        print("Comando invalido")