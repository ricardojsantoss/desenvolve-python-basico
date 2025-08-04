import random
from collections import Counter

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = sorted(set(lista1) & set(lista2))

contagem1 = Counter(lista1)
contagem2 = Counter(lista2)

print(f"lista1 = {lista1}")
print(f"lista2 = {lista2}")
print(f"Interseccao = {interseccao}")
print("\nContagem")
for numero in interseccao:
    print(f"{numero}: (lista1={contagem1[numero]}, lista2={contagem2[numero]})")