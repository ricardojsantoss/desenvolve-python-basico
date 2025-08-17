import os

frase = input("Digite uma frase: ")

# salva no mesmo diretório do script
caminho = os.path.join(os.getcwd(), "frase.txt")

with open(caminho, "w", encoding="utf-8") as f:
    f.write(frase)

print(f"Frase salva em {caminho}")