# Lê o comprimento do terreno
comp = int(input("Digite o comprimento do terreno (m): "))

# Lê a largura do terreno
larg = int(input("Digite a largura do terreno (m): "))

# Lê o preço do metro quadrado
preco_m2 = float(input("Digite o preço do metro quadrado (R$): "))

# Calcula a área do terreno
area = comp * larg

# Calcula o preço total do terreno
preco_total = preco_m2 * area

# Exibe a área e o valor total do terreno formatado
print(f"O terreno possui {area}m² e custa R${preco_total:,.2f}")