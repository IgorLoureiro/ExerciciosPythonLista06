CarlosSalario = 1500
JoaoSalario = CarlosSalario/3
SalarioCarlosConta = CarlosSalario
SalarioJoaoConta = JoaoSalario
i = 1

while SalarioCarlosConta > SalarioJoaoConta:
    SalarioCarlosConta = SalarioCarlosConta + (SalarioCarlosConta * 0.02)
    SalarioJoaoConta = SalarioJoaoConta + (SalarioJoaoConta * 0.05)

    i = i + 1

print(f"O numero de meses que ira demorar parar que a Conta de João tenha mais dinheiro que a de Carlos é de {i} meses")
