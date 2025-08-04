import random

lista = [random.randint(-100, 100) for _ in range(20)]

print("Lista ordenada (sem alterar original):", sorted(lista))
print("Lista original:", lista)
print("Índice do maior valor:", lista.index(max(lista)))
print("Índice do menor valor:", lista.index(min(lista)))