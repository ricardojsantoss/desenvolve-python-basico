import random
import unicodedata

def remover_acentos(s: str) -> str:
    """Remove acentos de uma string"""
    return "".join(ch for ch in unicodedata.normalize("NFD", s) if not unicodedata.combining(ch))

# === Leitura dos arquivos ===
def carregar_palavras(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f if linha.strip()]

def carregar_enforcado(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        conteudo = f.read().strip()
    return conteudo.split("\n\n")

# === Função para imprimir enforcado ===
def imprime_enforcado(estagios, erros):
    print(estagios[erros])

# === Programa principal ===
palavras = carregar_palavras("gabarito_forca.txt")
estagios = carregar_enforcado("gabarito_enforcado.txt")

# Sorteia palavra secreta
palavra_secreta = random.choice(palavras)
palavra_norm = remover_acentos(palavra_secreta).lower()

# Estado inicial
letras_certas = []
erros = 0
limite_erros = 6

print("=== Jogo da Forca ===")

while True:
    # Mostrar progresso
    exibicao = ""
    for i, letra in enumerate(palavra_secreta):
        if remover_acentos(letra).lower() in letras_certas:
            exibicao += letra
        else:
            exibicao += "_"
    print("\nPalavra:", " ".join(exibicao))

    # Vitória
    if "_" not in exibicao:
        print("🎉 Parabéns! Você venceu!")
        break

    # Derrota
    if erros >= limite_erros:
        imprime_enforcado(estagios, erros)
        print("💀 Você perdeu! A palavra era:", palavra_secreta)
        break

    # Mostrar enforcado atual
    imprime_enforcado(estagios, erros)

    # Entrada do jogador
    palpite = input("Digite uma letra: ").strip().lower()
    palpite_norm = remover_acentos(palpite)

    if len(palpite) != 1 or not palpite.isalpha():
        print("Digite apenas UMA letra válida.")
        continue

    if palpite_norm in letras_certas:
        print("Você já tentou essa letra.")
        continue

    # Verificar acerto
    if palpite_norm in palavra_norm:
        letras_certas.append(palpite_norm)
        print("✔️ Boa! A letra está na palavra.")
    else:
        erros += 1
        print("❌ Errou!")