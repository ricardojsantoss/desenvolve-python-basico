import csv

# (título, autor, ano, páginas)
livros = [
    ("1984", "George Orwell", 1949, 328),
    ("A revolução dos bichos", "George Orwell", 1945, 112),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96),
    ("Sapiens", "Yuval Noah Harari", 2011, 464),
    ("Homo Deus", "Yuval Noah Harari", 2015, 496),
    ("O diário de Anne Frank", "Anne Frank", 1947, 352),
    ("A Bailarina de Auschwitz", "Edith Eger", 2017, 368),
    ("A cabana", "William P. Young", 2007, 240),
    ("Uma breve história do tempo", "Stephen Hawking", 1988, 256),
    ("Vidas secas", "Graciliano Ramos", 1938, 175),
]

with open("meus_livros.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)  # separador = vírgula, como pede o enunciado
    w.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])
    for titulo, autor, ano, paginas in livros:
        w.writerow([titulo, autor, ano, paginas])

print("Arquivo 'meus_livros.csv' gerado com sucesso")
