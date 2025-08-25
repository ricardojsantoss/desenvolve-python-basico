import random

lista = [random.randint(-10, 10) for _ in range(20)]

print("Original:", lista)

inicio = fim = 0
melhor_inicio = melhor_fim = 0
i = 0

while i < len(lista):
    if lista[i] < 0:
        inicio = i
        while i < len(lista) and lista[i] < 0:
            i += 1
        fim = i
        if (fim - inicio) > (melhor_fim - melhor_inicio):
            melhor_inicio, melhor_fim = inicio, fim
    else:
        i += 1

del lista[melhor_inicio:melhor_fim]

print("Editada:", lista)