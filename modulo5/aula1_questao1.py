num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

diferenca = abs(num1 - num2)
diferenca_arredondada = round(diferenca, 2)

print(f"A diferença absoluta entre os números é: {diferenca_arredondada}")