frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
indices = [i for i, letra in enumerate(frase) if letra in vogais]

print(f"{len(indices)} vogais")
print(f"Índices {indices}")