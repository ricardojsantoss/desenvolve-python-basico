import random

def encrypt(lista):
    n = random.randint(1, 10)
    cript = []
    for nome in lista:
        novo = ""
        for c in nome:
            codigo = ord(c)
            novo += chr(((codigo - 33 + n) % 94) + 33)
        cript.append(novo)
    return cript, n

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave = encrypt(nomes)

print("Chave aleatória:", chave)
print("Nomes criptografados:", nomes_cript)