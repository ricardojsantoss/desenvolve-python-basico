lista1 = []
lista2 = []

qtd1 = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {qtd1} elementos da lista 1:")
for _ in range(qtd1):
    lista1.append(int(input()))

qtd2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {qtd2} elementos da lista 2:")
for _ in range(qtd2):
    lista2.append(int(input()))

lista_intercalada = []
for i in range(max(len(lista1), len(lista2))):
    if i < len(lista1):
        lista_intercalada.append(lista1[i])
    if i < len(lista2):
        lista_intercalada.append(lista2[i])

print("Lista intercalada:", *lista_intercalada)