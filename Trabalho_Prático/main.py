# Sistema de Cafeteria - Python Básico

import os

# Arquivos
usuarios_file = "usuarios.csv"
produtos_file = "produtos.csv"

# Usuários iniciais
usuarios_iniciais = [
    "admin,123,gerente\n",
    "atendente,123,atendente\n",
    "cliente,123,cliente\n"
]

# Produtos iniciais
produtos_iniciais = [
    "Café Expresso,5.0,10\n",
    "Cappuccino,7.5,8\n",
    "Pão de Queijo,4.0,15\n",
    "Bolo de Chocolate,6.0,6\n"
]

# Criar arquivos se não existirem
if not os.path.exists(usuarios_file):
    with open(usuarios_file, "w", encoding="utf-8") as f:
        f.writelines(usuarios_iniciais)

if not os.path.exists(produtos_file):
    with open(produtos_file, "w", encoding="utf-8") as f:
        f.writelines(produtos_iniciais)

# ------------------- Funções auxiliares -------------------

def carregar_usuarios():
    """
    Carrega os usuários do arquivo CSV.
    Entrada: nenhuma
    Saída: lista de dicionários contendo 'usuario', 'senha' e 'nivel'
    """
    usuarios = []
    with open(usuarios_file, "r", encoding="utf-8") as f:
        for linha in f:
            user, senha, nivel = linha.strip().split(",")
            usuarios.append({"usuario": user, "senha": senha, "nivel": nivel})
    return usuarios

def salvar_usuario(usuario, senha, nivel):
    """
    Salva um novo usuário no arquivo CSV.
    Entrada: usuario (str), senha (str), nivel (str)
    Saída: nenhum (grava no arquivo)
    """
    with open(usuarios_file, "a", encoding="utf-8") as f:
        f.write(f"{usuario},{senha},{nivel}\n")

def salvar_todos_usuarios(usuarios):
    """
    Sobrescreve todos os usuários no arquivo CSV.
    Entrada: lista de dicionários de usuários
    Saída: nenhum (grava no arquivo)
    """
    with open(usuarios_file, "w", encoding="utf-8") as f:
        for u in usuarios:
            f.write(f"{u['usuario']},{u['senha']},{u['nivel']}\n")

def listar_usuarios():
    """
    Lista todos os usuários cadastrados no sistema.
    Entrada: nenhuma
    Saída: impressão no console de cada usuário e seu nível
    """
    usuarios = carregar_usuarios()
    print("\n=== Usuários cadastrados ===")
    for u in usuarios:
        print(f"Usuário: {u['usuario']} - Nível: {u['nivel']}")

def atualizar_usuario():
    """
    Atualiza o nível de um usuário existente.
    Entrada: solicitada pelo input do usuário
    Saída: atualização no arquivo CSV e mensagem de confirmação ou erro
    """
    usuarios = carregar_usuarios()
    usuario_alvo = input("Digite o nome do usuário que deseja atualizar: ")
    for u in usuarios:
        if u["usuario"] == usuario_alvo:
            novo_nivel = input("Novo nível (gerente/atendente/cliente): ")
            u["nivel"] = novo_nivel
            salvar_todos_usuarios(usuarios)
            print("Nível de usuário atualizado!")
            return
    print("Usuário não encontrado!")

def excluir_usuario():
    """
    Exclui um usuário do sistema.
    Entrada: solicitada pelo input do usuário
    Saída: remoção do usuário do arquivo CSV e mensagem de confirmação ou erro
    """
    usuarios = carregar_usuarios()
    usuario_alvo = input("Digite o nome do usuário que deseja excluir: ")
    for u in usuarios:
        if u["usuario"] == usuario_alvo:
            usuarios.remove(u)
            salvar_todos_usuarios(usuarios)
            print("Usuário excluído!")
            return
    print("Usuário não encontrado!")

def alterar_senha(usuario_atual):
    """
    Permite ao usuário alterar sua própria senha.
    Entrada: usuário logado (str), nova senha solicitada via input
    Saída: atualização no arquivo CSV e mensagem de confirmação
    """
    usuarios = carregar_usuarios()
    for u in usuarios:
        if u["usuario"] == usuario_atual:
            nova_senha = input("Digite sua nova senha: ")
            u["senha"] = nova_senha
            salvar_todos_usuarios(usuarios)
            print("Senha alterada com sucesso!")
            return

def carregar_produtos():
    """
    Carrega os produtos do arquivo CSV.
    Entrada: nenhuma
    Saída: lista de dicionários com 'nome', 'preco' e 'estoque'
    """
    produtos = []
    with open(produtos_file, "r", encoding="utf-8") as f:
        for linha in f:
            nome, preco, estoque = linha.strip().split(",")
            produtos.append({"nome": nome, "preco": float(preco), "estoque": int(estoque)})
    return produtos

def salvar_produto(nome, preco, estoque):
    """
    Salva um novo produto no arquivo CSV.
    Entrada: nome (str), preco (float), estoque (int)
    Saída: nenhum (grava no arquivo)
    """
    with open(produtos_file, "a", encoding="utf-8") as f:
        f.write(f"{nome},{preco},{estoque}\n")

def salvar_todos_produtos(produtos):
    """
    Sobrescreve todos os produtos no arquivo CSV.
    Entrada: lista de dicionários de produtos
    Saída: nenhum (grava no arquivo)
    """
    with open(produtos_file, "w", encoding="utf-8") as f:
        for p in produtos:
            f.write(f"{p['nome']},{p['preco']},{p['estoque']}\n")

# ------------------- Menus -------------------

def menu_gerente(usuario_logado):
    while True:
        print("\n=== MENU GERENTE ===")
        print("--- Cafeteria / Vendas ---")
        print("1 - Listar produtos")
        print("2 - Cadastrar produto")
        print("3 - Atualizar estoque de produto")
        print("4 - Alterar preço de produto")
        print("5 - Excluir produto")
        print("--- Gerenciamento de usuários ---")
        print("6 - Listar usuários")
        print("7 - Adicionar novo usuário")
        print("8 - Atualizar nível de usuário")
        print("9 - Excluir usuário")
        print("--- Minha conta ---")
        print("10 - Alterar minha senha")
        print("0 - Sair")
        opcao = input("Escolha: ")

        produtos = carregar_produtos()
        usuarios = carregar_usuarios()

        # ---------- Cafeteria / Vendas ----------
        if opcao == "1":
            print("\nProdutos cadastrados:")
            for idx, p in enumerate(produtos, start=1):
                print(f"{idx} - {p['nome']} - R$ {p['preco']} - Estoque: {p['estoque']}")
        elif opcao == "2":
            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            estoque = int(input("Estoque: "))
            salvar_produto(nome, preco, estoque)
            print("Produto cadastrado com sucesso!")
        elif opcao == "3":
            print("\nProdutos disponíveis:")
            for idx, p in enumerate(produtos, start=1):
                print(f"{idx} - {p['nome']} - Estoque: {p['estoque']}")
            escolha_prod = input("Digite o número do produto para atualizar estoque: ")
            if escolha_prod.isdigit() and 1 <= int(escolha_prod) <= len(produtos):
                idx_prod = int(escolha_prod) - 1
                novo_estoque = int(input(f"Novo estoque para {produtos[idx_prod]['nome']}: "))
                produtos[idx_prod]['estoque'] = novo_estoque
                salvar_todos_produtos(produtos)
                print("Estoque atualizado!")
            else:
                print("Número inválido!")
        elif opcao == "4":  # Alterar preço
            print("\nProdutos disponíveis:")
            for idx, p in enumerate(produtos, start=1):
                print(f"{idx} - {p['nome']} - R$ {p['preco']}")
            escolha_prod = input("Digite o número do produto para alterar o preço: ")
            if escolha_prod.isdigit() and 1 <= int(escolha_prod) <= len(produtos):
                idx_prod = int(escolha_prod) - 1
                novo_preco = float(input(f"Novo preço para {produtos[idx_prod]['nome']}: "))
                produtos[idx_prod]['preco'] = novo_preco
                salvar_todos_produtos(produtos)
                print("Preço atualizado!")
            else:
                print("Número inválido!")
        elif opcao == "5":  # Excluir produto
            print("\nProdutos disponíveis:")
            for idx, p in enumerate(produtos, start=1):
                print(f"{idx} - {p['nome']} - R$ {p['preco']}")
            escolha_prod = input("Digite o número do produto que deseja excluir: ")
            if escolha_prod.isdigit() and 1 <= int(escolha_prod) <= len(produtos):
                idx_prod = int(escolha_prod) - 1
                excluido = produtos.pop(idx_prod)
                salvar_todos_produtos(produtos)
                print(f"Produto {excluido['nome']} excluído!")
            else:
                print("Número inválido!")

        # ---------- Gerenciamento de usuários ----------
        elif opcao == "6":
            print("\nUsuários cadastrados:")
            for idx, u in enumerate(usuarios, start=1):
                print(f"{idx} - Usuário: {u['usuario']} - Nível: {u['nivel']}")
        elif opcao == "7":
            usuario = input("Novo usuário: ")
            senha = input("Senha: ")
            nivel = input("Nível (gerente/atendente/cliente): ")
            salvar_usuario(usuario, senha, nivel)
            print("Usuário cadastrado com sucesso!")
        elif opcao == "8":
            print("\nUsuários cadastrados:")
            for idx, u in enumerate(usuarios, start=1):
                print(f"{idx} - Usuário: {u['usuario']} - Nível: {u['nivel']}")
            escolha = input("Digite o número do usuário que deseja atualizar: ")
            if escolha.isdigit() and 1 <= int(escolha) <= len(usuarios):
                idx_usuario = int(escolha) - 1
                novo_nivel = input(f"Novo nível para {usuarios[idx_usuario]['usuario']} (gerente/atendente/cliente): ")
                usuarios[idx_usuario]['nivel'] = novo_nivel
                salvar_todos_usuarios(usuarios)
                print("Nível de usuário atualizado!")
            else:
                print("Número inválido!")
        elif opcao == "9":
            print("\nUsuários cadastrados:")
            for idx, u in enumerate(usuarios, start=1):
                print(f"{idx} - Usuário: {u['usuario']} - Nível: {u['nivel']}")
            escolha = input("Digite o número do usuário que deseja excluir: ")
            if escolha.isdigit() and 1 <= int(escolha) <= len(usuarios):
                idx_usuario = int(escolha) - 1
                excluido = usuarios.pop(idx_usuario)
                salvar_todos_usuarios(usuarios)
                print(f"Usuário {excluido['usuario']} excluído!")
            else:
                print("Número inválido!")

        # ---------- Minha conta ----------
        elif opcao == "10":
            alterar_senha(usuario_logado)

        # ---------- Sair ----------
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def menu_atendente(usuario_logado):
    while True:
        print("\n=== MENU ATENDENTE ===")
        print("1 - Listar produtos")
        print("2 - Atualizar estoque")
        print("3 - Alterar minha senha")
        print("0 - Sair")
        opcao = input("Escolha: ")

        produtos = carregar_produtos()

        if opcao == "1":
            print("\nProdutos disponíveis:")
            for idx, p in enumerate(produtos, start=1):
                print(f"{idx} - {p['nome']} - R$ {p['preco']} - Estoque: {p['estoque']}")

        elif opcao == "2":
            print("\nProdutos disponíveis:")
            for idx, p in enumerate(produtos, start=1):
                print(f"{idx} - {p['nome']} - Estoque: {p['estoque']}")
            escolha_prod = input("Digite o número do produto para atualizar estoque: ")
            if escolha_prod.isdigit() and 1 <= int(escolha_prod) <= len(produtos):
                idx_prod = int(escolha_prod) - 1
                novo_estoque = int(input(f"Novo estoque para {produtos[idx_prod]['nome']}: "))
                produtos[idx_prod]['estoque'] = novo_estoque
                salvar_todos_produtos(produtos)
                print("Estoque atualizado!")
            else:
                print("Número inválido!")

        elif opcao == "3":
            alterar_senha(usuario_logado)

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def menu_cliente(usuario_logado):
    while True:
        print("\n=== MENU CLIENTE ===")
        print("1 - Listar produtos")
        print("2 - Comprar produtos")
        print("3 - Alterar minha senha")
        print("0 - Sair")
        opcao = input("Escolha: ")

        produtos = carregar_produtos()

        if opcao == "1":
            print("\nCardápio da cafeteria:")
            for idx, p in enumerate(produtos, start=1):
                print(f"{idx} - {p['nome']} - R$ {p['preco']} - Estoque: {p['estoque']}")

        elif opcao == "2":
            carrinho = []
            while True:
                print("\nProdutos disponíveis:")
                for idx, p in enumerate(produtos, start=1):
                    print(f"{idx} - {p['nome']} - R$ {p['preco']} - Estoque: {p['estoque']}")

                escolha_prod = input("Digite o número do produto que deseja comprar (0 para finalizar): ")
                if escolha_prod == "0":
                    break

                if not escolha_prod.isdigit() or int(escolha_prod) < 1 or int(escolha_prod) > len(produtos):
                    print("Número inválido!")
                    continue

                idx_prod = int(escolha_prod) - 1
                produto = produtos[idx_prod]

                qtd = input(f"Quantos {produto['nome']} deseja comprar? ")
                if not qtd.isdigit() or int(qtd) < 1:
                    print("Quantidade inválida!")
                    continue

                qtd = int(qtd)
                if qtd > produto['estoque']:
                    print(f"Não há estoque suficiente! Estoque disponível: {produto['estoque']}")
                    continue

                carrinho.append({"nome": produto['nome'], "preco": produto['preco'], "quantidade": qtd})
                produto['estoque'] -= qtd
                salvar_todos_produtos(produtos)
                print(f"{qtd} {produto['nome']} adicionados ao carrinho!")

                mais = input("Deseja adicionar outro produto? (s/n): ").lower()
                if mais != 's':
                    break

            if carrinho:
                total = sum(item['preco'] * item['quantidade'] for item in carrinho)
                print("\n=== Resumo da compra ===")
                for item in carrinho:
                    print(f"{item['quantidade']}x {item['nome']} - R$ {item['preco']} cada")
                print(f"Total a pagar: R$ {total:.2f}")
                print("Obrigado pela compra!")

        elif opcao == "3":
            alterar_senha(usuario_logado)

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

# ------------------- Login -------------------

def login():
    usuarios = carregar_usuarios()
    user = input("Usuário: ")
    senha = input("Senha: ")
    for u in usuarios:
        if u["usuario"] == user and u["senha"] == senha:
            print(f"\nBem-vindo, {u['usuario']}! Seu nível é {u['nivel']}.")
            if u["nivel"] == "gerente":
                menu_gerente(user)
            elif u["nivel"] == "atendente":
                menu_atendente(user)
            elif u["nivel"] == "cliente":
                menu_cliente(user)
            return
    print("Usuário ou senha inválidos!")

# ------------------- Programa principal -------------------

while True:
    print("\n=== SISTEMA DA CAFETERIA ===")
    print("1 - Login")
    print("0 - Sair")
    escolha = input("Escolha: ")

    if escolha == "1":
        login()
    elif escolha == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")