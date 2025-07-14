idade = int(input("Digite sua idade: "))
ja_jogou = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ") == "True"
vitorias = int(input("Quantos jogos já venceu? "))

apto = 16 <= idade <= 18 and ja_jogou and vitorias >= 1
print("Apto para ingressar no clube de jogos de tabuleiro:", apto)