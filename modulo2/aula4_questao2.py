# Lê a temperatura em Fahrenheit (inteiro)
f = int(input("Digite a temperatura em Fahrenheit: "))

# Converte para Celsius com a fórmula
c = (f - 32) * (5/9)

# Converte para inteiro
c_int = int(c)

# Exibe o resultado formatado
print(f"{f} graus Fahrenheit são {c_int} graus Celsius.")