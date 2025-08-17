import string

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == "fim":
        break

    # Remove espaços e pontuação
    limpa = "".join(c.lower() for c in frase if c.isalnum())

    if limpa == limpa[::-1]:
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')