n = int(input("Quantos respondentes participaram da pesquisa? "))
soma_idades = 0
cont = 0

while cont < n:
    idade = int(input(f"Digite a idade do respondente {cont + 1}: "))
    soma_idades += idade
    cont += 1

media = soma_idades / n
print("Média das idades:", media)