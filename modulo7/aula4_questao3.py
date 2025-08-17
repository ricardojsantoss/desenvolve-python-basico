import re

with open("estomago.txt", "r") as f:
    linhas = f.readlines()

# primeiras 25 linhas
print("Primeiras 25 linhas:\n")
print("".join(linhas[:25]))

# número de linhas
print("\nNúmero de linhas:", len(linhas))

# linha com maior número de caracteres
maior = max(linhas, key=len)
print("\nLinha mais longa:", maior.strip())

# contagem de personagens
texto = "".join(linhas).lower()
n_nonato = len(re.findall(r"\bnonato\b", texto, re.IGNORECASE))
n_iria = len(re.findall(r"\bíria\b", texto, re.IGNORECASE))

print(f"\nMenções a Nonato: {n_nonato}")
print(f"Menções a Íria: {n_iria}")