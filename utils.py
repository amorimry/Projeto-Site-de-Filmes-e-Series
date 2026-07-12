from classes import Filme, Serie

def escolher_assistido_ou_nao(complemento1, complemento2):
    while True:
        try:
            escolha = int(input(f"""O que você deseja adicionar?
                            
    1. {complemento1}
    2. {complemento2}

--> """))
            if escolha in [1, 2]:
                return escolha
            else:
                print("Opção inválida. Por favor, digite 1 ou 2.")
        except ValueError:
            print("Opção inválida. Por favor, digite 1 ou 2.")

#-------------------------------------------------------------------------

def escolher_listar_assistido_ou_nao(complemento1, complemento2):
    while True:
        try:
            escolha = int(input(f"""O que você deseja listar?
                        
    1. {complemento1}
    2. {complemento2}

--> """))
            if escolha in [1, 2]:
                return escolha
            else:
                print("Opção inválida. Por favor, digite 1 ou 2.")
        except ValueError:
                print("Opção inválida. Por favor, digite 1 ou 2.")

#-------------------------------------------------------------------------

def adicionar_filme():
    while True:
        titulo = input("Digite o título do filme: ")
        if titulo.strip() == "":
            print("O título não pode estar vazio. Por favor, digite um título válido.")
            continue
        else:
            break
    while True:
        ano = input("Digite o ano de lançamento do filme: ")
        if not ano.isdigit() or len(ano) != 4:
            print("Ano inválido. Por favor, digite um ano válido com 4 dígitos.")
            continue
        else:
            break
    while True:
        duracao = input("Digite a duração do filme (em minutos): ")
        if not duracao.isdigit():
            print("Duração inválida. Por favor, digite um número válido.")
            continue
        else:
            break
    while True:
        genero = input("Digite o gênero do filme: ")
        if genero.strip() == "":
            print("O gênero não pode estar vazio. Por favor, digite um gênero válido.")
            continue
        else:
            break
    while True:
        sinopse = input("Digite a sinopse do filme: ")
        if sinopse.strip() == "":
            print("A sinopse não pode estar vazia. Por favor, digite uma sinopse válida.")
            continue
        else:
            break

    return {
        "titulo": titulo.title(),
        "ano": ano,
        "duracao": duracao,
        "genero": genero.title(),
        "sinopse": sinopse.title()
    }

def adicionar_serie():
    while True:
        titulo = input("Digite o título da série: ")
        if titulo.strip() == "":
            print("O título não pode estar vazio. Por favor, digite um título válido.")
            continue
        else:
            break
    while True:
        ano = input("Digite o ano de lançamento da série: ")
        if not ano.isdigit() or len(ano) != 4:
            print("Ano inválido. Por favor, digite um ano válido com 4 dígitos.")
            continue
        else:
            break
    while True:
        temporadas = input("Digite o número de temporadas da série: ")
        if not temporadas.isdigit():
            print("Número de temporadas inválido. Por favor, digite um número válido.")
            continue
        else:
            break
    while True:
        genero = input("Digite o gênero da série: ")
        if genero.strip() == "":
            print("O gênero não pode estar vazio. Por favor, digite um gênero válido.")
            continue
        else:
            break
    while True:
        sinopse = input("Digite a sinopse da série: ")
        if sinopse.strip() == "":
            print("A sinopse não pode estar vazia. Por favor, digite uma sinopse válida.")
            continue
        else:
            break

    return {
        "titulo": titulo.title(),
        "ano": ano,
        "temporadas": temporadas,
        "genero": genero.title(),
        "sinopse": sinopse.title()
    }

#-------------------------------------------------------------------------

def listar_filmes(ass_sim_nao, lista):
    print(f"""
    -- Lista de filmes {ass_sim_nao} --
""")
    for i, filme in enumerate(lista):
        print(f"{i+1} - {filme.titulo}")

def listar_series(ass_sim_nao, lista):
    print(f"""
    -- Lista de séries {ass_sim_nao} --
""")
    for i, serie in enumerate(lista):
        print(f"{i+1} - {serie.titulo}")

#-------------------------------------------------------------------------

def parte2_da_lista_filmes(ass_sim_nao, lista_filmes_assistidos, lista_filmes_nao_assistidos):
    if ass_sim_nao == "assistidos":
        while True:
            op = input(f"""O que deseja fazer agora?

        1 - Voltar ao menu principal
        2 - Ver informações detalhadas de um filme
        3 - Marcar um filme como não assistido
    --> """)
            if op == "1":
                input("Pressione Enter para continuar...")
                return
            elif op == "2":
                while True:
                    try:
                        op2 = int(input("Digite o número do filme que deseja ver as informações detalhadas: "))
                        op2 = op2 - 1
                        if op2 < 0 or op2 >= len(lista_filmes_assistidos):
                            print("Número inválido. Por favor, digite um número válido.")
                            continue
                        else:
                            lista_filmes_assistidos[op2].exibir_filme()
                            input("Pressione Enter para continuar...")
                            break
                    except ValueError:
                        print("Número inválido. Por favor, digite um número válido.")
            elif op == "3":
                while True:
                    try:
                        op3 = int(input(f"Digite o número do filme que deseja marcar como não assistido: "))
                        op3 = op3 - 1
                        if op3 < 0 or op3 >= len(lista_filmes_assistidos):
                            print("Número inválido. Por favor, digite um número válido.")
                            continue
                        else:
                            filme = lista_filmes_assistidos.pop(op3)
                            filme.assistido = False
                            lista_filmes_nao_assistidos.append(filme)
                            print(f"Filme '{filme.titulo}' marcado como não assistido.")
                            break
                    except ValueError:
                        print("Número inválido. Por favor, digite um número válido.")
            else:
                print("Opção inválida. Por favor, digite 1, 2 ou 3.")

    if ass_sim_nao == "não assistidos":
        while True:
            op = input(f"""O que deseja fazer agora?

        1 - Voltar ao menu principal
        2 - Ver informações detalhadas de um filme
        3 - Marcar um filme como assistido
    --> """)
            if op == "1":
                input("Pressione Enter para continuar...")
                return
            elif op == "2":
                while True:
                    try:
                        op2 = int(input("Digite o número do filme que deseja ver as informações detalhadas: "))
                        op2 = op2 - 1
                        if op2 < 0 or op2 >= len(lista_filmes_assistidos):
                            print("Número inválido. Por favor, digite um número válido.")
                            continue
                        else:
                            lista_filmes_assistidos[op2].exibir_filme()
                            input("Pressione Enter para continuar...")
                            break
                    except ValueError:
                        print("Número inválido. Por favor, digite um número válido.")
            elif op == "3":
                while True:
                    try:
                        op3 = int(input(f"Digite o número do filme que deseja marcar como assistido: "))
                        op3 = op3 - 1
                        if op3 < 0 or op3 >= len(lista_filmes_nao_assistidos):
                            print("Número inválido. Por favor, digite um número válido.")
                            continue
                        else:
                            filme = lista_filmes_nao_assistidos.pop(op3)
                            filme.assistido = True
                            lista_filmes_assistidos.append(filme)
                            print(f"Filme '{filme.titulo}' marcado como assistido.")
                            break
                    except ValueError:
                        print("Número inválido. Por favor, digite um número válido.")
            else:
                print("Opção inválida. Por favor, digite 1, 2 ou 3.")

def parte2_da_lista_series(ass_sim_nao, lista_series_assistidas, lista_series_nao_assistidas):
    if ass_sim_nao == "assistidas":
        while True:
            op = input(f"""O que deseja fazer agora?

        1 - Voltar ao menu principal
        2 - Ver informações detalhadas de uma série
        3 - Marcar uma série como não assistida
    --> """)
            if op == "1":
                input("Pressione Enter para continuar...")
                return
            elif op == "2":
                while True:
                    try:
                        op2 = int(input("Digite o número da série que deseja ver as informações detalhadas: "))
                        op2 = op2 - 1
                        if op2 < 0 or op2 >= len(lista_series_assistidas):
                            print("Número inválido. Por favor, digite um número válido.")
                            continue
                        else:
                            lista_series_assistidas[op2].exibir_serie()
                            input("Pressione Enter para continuar...")
                            break
                    except ValueError:
                        print("Número inválido. Por favor, digite um número válido.")
            elif op == "3":
                while True:
                    try:
                        op3 = int(input(f"Digite o número da série que deseja marcar como não assistida: "))
                        op3 = op3 - 1
                        if op3 < 0 or op3 > len(lista_series_assistidas):
                            print("Número inválido. Por favor, digite um número válido.")
                            continue
                        else:
                            serie = lista_series_assistidas.pop(op3)
                            serie.assistido = False
                            lista_series_nao_assistidas.append(serie)
                            print(f"Série '{serie.titulo}' marcada como não assistida.")
                            break
                    except ValueError:
                        print("Número inválido. Por favor, digite um número válido.")
            else:
                print("Opção inválida. Por favor, digite 1, 2 ou 3.")

    if ass_sim_nao == "não assistidas":
        while True:
            op = input(f"""O que deseja fazer agora?

        1 - Voltar ao menu principal
        2 - Ver informações detalhadas de uma série
        3 - Marcar uma série como assistida
    --> """)
            if op == "1":
                input("Pressione Enter para continuar...")
                return
            elif op == "2":
                while True:
                    try:
                        op2 = int(input("Digite o número da série que deseja ver as informações detalhadas: "))
                        op2 = op2 - 1
                        if op2 < 0 or op2 >= len(lista_series_nao_assistidas):
                            print("Número inválido. Por favor, digite um número válido.")
                            continue
                        else:
                            lista_series_nao_assistidas[op2].exibir_serie()
                            input("Pressione Enter para continuar...")
                            break
                    except ValueError:
                        print("Número inválido. Por favor, digite um número válido.")
            elif op == "3":
                while True:
                    try:
                        op3 = int(input(f"Digite o número da série que deseja marcar como assistida: "))
                        op3 = op3 - 1
                        if op3 < 0 or op3 >= len(lista_series_nao_assistidas):
                            print("Número inválido. Por favor, digite um número válido.")
                            continue
                        else:
                            serie = lista_series_nao_assistidas.pop(op3)
                            serie.assistido = True
                            lista_series_assistidas.append(serie)
                            print(f"Série '{serie.titulo}' marcada como assistida.")
                            break
                    except ValueError:
                        print("Número inválido. Por favor, digite um número válido.")
            else:
                print("Opção inválida. Por favor, digite 1, 2 ou 3.")