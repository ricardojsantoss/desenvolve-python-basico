# Lista de pares entre 20 e 50
pares = [x for x in range(20, 51) if x % 2 == 0]
print("Pares:", pares)

# Quadrados da lista [1,2,3,4,5,6,7,8,9]
quadrados = [x**2 for x in [1,2,3,4,5,6,7,8,9]]
print("Quadrados:", quadrados)

# Números entre 1 e 100 divisíveis por 7
divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]
print("Divisíveis por 7:", divisiveis_por_7)

# "par" ou "ímpar" para valores em range(0,30,3)
par_ou_impar = ['par' if x % 2 == 0 else 'ímpar' for x in range(0, 30, 3)]
print("Par ou ímpar:", par_ou_impar)