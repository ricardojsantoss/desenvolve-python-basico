def calcular_digito(cpf, multiplicadores):
    soma = sum(int(cpf[i]) * multiplicadores[i] for i in range(len(multiplicadores)))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")
cpf_numeros = "".join([c for c in cpf if c.isdigit()])

if len(cpf_numeros) != 11:
    print("Inválido")
else:
    primeiros9 = cpf_numeros[:9]
    dig1 = calcular_digito(primeiros9, list(range(10, 1, -1)))
    dig2 = calcular_digito(primeiros9 + str(dig1), list(range(11, 1, -1)))
    
    if cpf_numeros[-2:] == f"{dig1}{dig2}":
        print("Válido")
    else:
        print("Inválido")