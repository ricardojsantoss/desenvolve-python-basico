import random

num_elementos = random.randint(5, 20)
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

print("Lista elementos:", elementos)
print("Soma:", sum(elementos))
print("Média:", sum(elementos) / len(elementos))