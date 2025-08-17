data = input("Digite uma data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = data.split("/")

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

print(f"Você nasceu em {dia} de {meses[int(mes) - 1]} de {ano}.")