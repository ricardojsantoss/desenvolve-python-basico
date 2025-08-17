import re

# lê o arquivo frase.txt
with open("frase.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

# mantém apenas letras e espaços
palavras = re.findall(r"[A-Za-zÀ-ÿ]+", conteudo)

# salva cada palavra em uma linha
with open("palavras.txt", "w", encoding="utf-8") as f:
    for palavra in palavras:
        f.write(palavra + "\n")

# imprime o conteúdo salvo
with open("palavras.txt", "r", encoding="utf-8") as f:
    print(f.read())