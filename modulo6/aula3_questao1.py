numeros = []
print("Digite pelo menos 4 números inteiros (digite 'sair' para parar):")

while True:
    valor = input("Número: ")
    if valor.lower() == "sair":
        if len(numeros) >= 4:
            break
        else:
            print("Você precisa digitar pelo menos 4 números antes de sair!")
            continue
    try:
        numeros.append(int(valor))
    except ValueError:
        print("Digite apenas números inteiros ou 'sair'.")

print("\nLista original:", numeros)
print("3 primeiros elementos:", numeros[:3])
print("2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Índices pares:", numeros[::2])
print("Índices ímpares:", numeros[1::2])