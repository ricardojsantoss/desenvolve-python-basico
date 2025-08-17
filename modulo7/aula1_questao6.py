from collections import Counter

frase = input("Digite uma frase: ")
objetivo = input("Digite a palavra objetivo: ")

contador_obj = Counter(objetivo.lower())
palavras = frase.split()

anagramas = [p for p in palavras if Counter(p.lower()) == contador_obj]

print("Anagramas:", anagramas)