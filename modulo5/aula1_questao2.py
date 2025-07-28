import random
import math

n = int(input("Quantos números aleatórios você deseja gerar? "))
soma = 0

for _ in range(n):
    valor = random.randint(0, 100)
    print (valor)
    soma += valor

raiz = math.sqrt(soma)

print (soma)
print(f"A raiz quadrada da soma dos valores é: {round(raiz, 2)}")