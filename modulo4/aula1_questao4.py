n = int(input("Quantos números deseja digitar? "))
maior = 0

while n > 0:
    x = int(input("Digite um número: "))
    if x > maior:
        maior = x
    n = n - 1

print("Maior número digitado:", maior)