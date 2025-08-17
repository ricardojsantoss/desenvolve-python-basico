numero = input("Digite o número: ")

if len(numero) == 8:
    numero = "9" + numero
elif len(numero) == 9 and numero[0] != "9":
    numero = "9" + numero[1:]

numero_formatado = numero[:5] + "-" + numero[5:]
print(f"Número completo: {numero_formatado}")