from classes import Filme, Serie
import utils

lista_filmes_assistidos = [
      Filme("Interestelar", 2014, 169, "Ficção Científica", "Astronautas viajam pelo espaço em busca de um novo lar para a humanidade.", True),

      Filme("Clube da Luta", 1999, 139, "Drama", "Um homem insatisfeito cria um clube secreto de lutas.", True),

      Filme("Vingadores: Ultimato", 2019, 181, "Ação", "Os heróis enfrentam Thanos em sua batalha final.", True),

      Filme("O Rei Leão", 1994, 88, "Animação", "Simba enfrenta desafios para assumir o trono.", True),

      Filme("Matrix", 1999, 136, "Ficção Científica", "Um programador descobre que vive em uma simulação.", True)
]
lista_filmes_nao_assistidos = [
      Filme("Oppenheimer", 2023, 180, "Drama", "A história do criador da bomba atômica.", False),

      Filme("Duna: Parte Dois", 2024, 166, "Ficção Científica", "Paul Atreides continua sua jornada em Arrakis.", False),

      Filme("Parasita", 2019, 132, "Suspense", "Uma família pobre se infiltra na vida de uma família rica.", False),

      Filme("Blade Runner 2049", 2017, 164, "Ficção Científica", "Um novo blade runner descobre um segredo perigoso.", False),

      Filme("Whiplash", 2014, 107, "Drama", "Um jovem baterista busca a perfeição.", False)
]

lista_series_assistidas = [
      Serie("Breaking Bad", 2008, 5, "Drama", "Um professor de química entra para o tráfico de drogas.", True),

      Serie("Dark", 2017, 3, "Ficção Científica", "Mistérios envolvendo viagens no tempo.", True),

      Serie("Stranger Things", 2016, 5, "Suspense", "Crianças enfrentam criaturas de outra dimensão.", True),

      Serie("The Office", 2005, 9, "Comédia", "O cotidiano de um escritório cheio de situações engraçadas.", True),

      Serie("Arcane", 2021, 2, "Animação", "Conflitos entre Piltover e Zaun.", True)
]
lista_series_nao_assistidas = [
      Serie("The Last of Us", 2023, 2, "Drama", "Sobreviventes enfrentam um mundo devastado por um fungo.", False),

      Serie("House of the Dragon", 2022, 2, "Fantasia", "A guerra civil da Casa Targaryen.", False),

      Serie("Severance", 2022, 2, "Suspense", "Funcionários têm suas memórias divididas entre trabalho e vida pessoal.", False),

      Serie("The Bear", 2022, 4, "Drama", "Um chef tenta salvar o restaurante da família.", False),

      Serie("One Piece", 1999, 22, "Anime", "Luffy reúne sua tripulação em busca do One Piece.", False)
]

print()
print(f"{"="*5} Bem vindo ao seu site de organização de filmes e séries! {"="*5}")
while True:
      print("""
      -- MENU --

Escolha uma opção:
          
      1 - Adicionar filme
      2 - Adicionar série
      3 - Listar filmes
      4 - Listar séries
      5 - Editar filme
      6 - Editar série
      
      -- NÃO FUNCIONANDO AINDA --
      7 - Remover filme
      8 - Remover série

      0 - Sair
""")
      opcao = input("Digite o número da opção desejada: ")

      if opcao == "1":
            print("\n   Adicionando um novo filme...")
            print()
            escolha = utils.escolher_assistido_ou_nao("Filme assistido", "Filme não assistido")
            print()
            if escolha == 1:
                  dados_do_filme = utils.adicionar_filme()
                  novo_filme = Filme(
                        titulo=dados_do_filme["titulo"],
                        ano=dados_do_filme["ano"],
                        duracao=dados_do_filme["duracao"],
                        genero=dados_do_filme["genero"],
                        sinopse=dados_do_filme["sinopse"],
                        assistido=True
                        )
                  lista_filmes_assistidos.append(novo_filme)
                  print()
                  print(f"    Filme '{dados_do_filme['titulo'].title()}' adicionado à lista de filmes assistidos.")
                  print()
                  input("Pressione Enter para continuar...")

            if escolha == 2:
                  dados_do_filme = utils.adicionar_filme()
                  novo_filme = Filme(
                        titulo=dados_do_filme["titulo"],
                        ano=dados_do_filme["ano"],
                        duracao=dados_do_filme["duracao"],
                        genero=dados_do_filme["genero"],
                        sinopse=dados_do_filme["sinopse"],
                        assistido=False
                        )
                  lista_filmes_nao_assistidos.append(novo_filme)
                  print(f"    Filme '{dados_do_filme['titulo'].title()}' adicionado à lista de filmes não assistidos.")
                  print()
                  input("Pressione Enter para continuar...")

      elif opcao == "2":
            print("\n   Adicionando uma nova série...")
            print()
            escolha = utils.escolher_assistido_ou_nao("Série assistida", "Série não assistida")
            print()
            if escolha == 1:
                  dados_da_serie = utils.adicionar_serie()
                  nova_serie = Serie(
                        titulo=dados_da_serie["titulo"],
                        ano=dados_da_serie["ano"],
                        temporadas=dados_da_serie["temporadas"],
                        genero=dados_da_serie["genero"],
                        sinopse=dados_da_serie["sinopse"],
                        assistido=True
                        )
                  lista_series_assistidas.append(nova_serie)
                  print(f"    Série '{dados_da_serie['titulo'].title()}' adicionada à lista de séries assistidas.")
                  print()
                  input("Pressione Enter para continuar...")

            if escolha == 2:
                  dados_da_serie = utils.adicionar_serie()
                  nova_serie = Serie(
                        titulo=dados_da_serie["titulo"],
                        ano=dados_da_serie["ano"],
                        temporadas=dados_da_serie["temporadas"],
                        genero=dados_da_serie["genero"],
                        sinopse=dados_da_serie["sinopse"],
                        assistido=False
                        )
                  lista_series_nao_assistidas.append(nova_serie)
                  print(f"    Série '{dados_da_serie['titulo'].title()}' adicionada à lista de séries não assistidas.")
                  print()
                  input("Pressione Enter para continuar...")

      elif opcao == "3":
            print("\n   Listando filmes...")
            escolha = utils.escolher_listar_assistido_ou_nao("Filmes assistidos", "Filmes não assistidos")
            
            if escolha == 1:
                  if len(lista_filmes_assistidos) == 0:
                        print("\nNão há filmes assistidos na lista.")
                        print()
                        input("Pressione Enter para continuar...")
                        continue
                  else:
                        utils.listar_filmes("assistidos", lista_filmes_assistidos)
                        print()
                        input("Pressione Enter para continuar...")
                        
                        utils.parte2_da_lista_filmes("assistidos", lista_filmes_assistidos, lista_filmes_nao_assistidos)

            if escolha == 2:
                  if len(lista_filmes_nao_assistidos) == 0:
                        print("\nNão há filmes não assistidos na lista.")
                        print()
                        input("Pressione Enter para continuar...")
                        continue
                  else:
                        utils.listar_filmes("não assistidos", lista_filmes_nao_assistidos)
                        print()
                        input("Pressione Enter para continuar...")
                        
                        utils.parte2_da_lista_filmes("não assistidos", lista_filmes_assistidos, lista_filmes_nao_assistidos)

      elif opcao == "4":
            print("\n   Listando séries...")
            escolha = utils.escolher_listar_assistido_ou_nao("Séries assistidas", "Séries não assistidas")
            
            if escolha == 1:
                  if len(lista_series_assistidas) == 0:
                        print("\nNão há séries assistidas na lista.")
                        print()
                        input("Pressione Enter para continuar...")
                        continue
                  else:
                        utils.listar_series("assistidas", lista_series_assistidas)
                        print()
                        input("Pressione Enter para continuar...")
                        
                        utils.parte2_da_lista_series("assistidas", lista_series_assistidas, lista_series_nao_assistidas)

            if escolha == 2:
                  if len(lista_series_nao_assistidas) == 0:
                        print("\nNão há séries não assistidas na lista.")
                        print()
                        input("Pressione Enter para continuar...")
                        continue
                  else:
                        utils.listar_series("não assistidas", lista_series_nao_assistidas)
                        print()
                        input("Pressione Enter para continuar...")
                        
                        utils.parte2_da_lista_series("não assistidas", lista_series_assistidas, lista_series_nao_assistidas)

      elif opcao == "5":
            print("\n   Editando filme...")

            escolha = utils.escolher_assistido_ou_nao("Filme assistido", "Filme não assistido")

            if escolha == 1:
                  if len(lista_filmes_assistidos) == 0:
                        print("\nNão há filmes assistidos na lista.")
                        print()
                        input("Pressione Enter para continuar...")
                        continue
                  else:
                        while True:
                              utils.listar_filmes("assistidos", lista_filmes_assistidos)
                              print()
                              input("Pressione Enter para continuar...")
                              print()
                              utils.editar_filme(lista_filmes_assistidos)

                              continuar = input("\nDeseja editar outro campo? (s/n): ").strip().lower()
                              if continuar in ["s", "sim"]:
                                    continue
                              elif continuar in ["n", "nao", "não"]:
                                    input("Pressione Enter para voltar ao menu...")
                                    break
                              else:
                                    print("Entrada inválida. Digite 's' ou 'n'.")
            if escolha == 2:
                  if len(lista_filmes_nao_assistidos) == 0:
                        print("\nNão há filmes não assistidos na lista.")
                        print()
                        input("Pressione Enter para continuar...")
                        continue
                  else:
                        while True:
                              utils.listar_filmes("não assistidos", lista_filmes_nao_assistidos)
                              print()
                              input("Pressione Enter para continuar...")
                              print()
                              utils.editar_filme(lista_filmes_nao_assistidos)

                              continuar = input("\nDeseja editar outro campo? (s/n): ").strip().lower()
                              if continuar in ["s", "sim"]:
                                    continue
                              elif continuar in ["n", "nao", "não"]:
                                    input("Pressione Enter para voltar ao menu...")
                                    break
                              else:
                                    print("Entrada inválida. Digite 's' ou 'n'.")

      elif opcao == "6":
            print("\n   Editando série...")

            escolha = utils.escolher_assistido_ou_nao("Série assistida", "Série não assistida")

            if escolha == 1:
                  if len(lista_series_assistidas) == 0:
                        print("\nNão há séries assistidas na lista.")
                        print()
                        input("Pressione Enter para continuar...")
                        continue
                  else:
                        while True:
                              utils.listar_series("não assistidas", lista_series_assistidas)
                              print()
                              input("Pressione Enter para continuar...")
                              print()
                              utils.editar_serie(lista_series_assistidas)

                              continuar = input("\nDeseja editar outro campo? (s/n): ").strip().lower()
                              if continuar in ["s", "sim"]:
                                    continue
                              elif continuar in ["n", "nao", "não"]:
                                    input("Pressione Enter para voltar ao menu...")
                                    break
                              else:
                                    print("Entrada inválida. Digite 's' ou 'n'.")

            if escolha == 2:
                  if len(lista_series_nao_assistidas) == 0:
                        print("\nNão há séries não assistidas na lista.")
                        print()
                        input("Pressione Enter para continuar...")
                        continue
                  else:
                        while True:
                              utils.listar_series("não assistidas", lista_series_nao_assistidas)
                              print()
                              input("Pressione Enter para continuar...")
                              print()
                              utils.editar_serie(lista_series_nao_assistidas)

                              continuar = input("\nDeseja editar outro campo? (s/n): ").strip().lower()
                              if continuar in ["s", "sim"]:
                                    continue
                              elif continuar in ["n", "nao", "não"]:
                                    input("Pressione Enter para voltar ao menu...")
                                    break
                              else:
                                    print("Entrada inválida. Digite 's' ou 'n'.")

      elif opcao == "7":
            print("\n   Removendo filme...")

      elif opcao == "8":
            print("\n   Removendo série...")

      elif opcao == "0":
            print()
            input("Saindo do programa, digite Enter para confirmar 👋...")
            print()
            break

      else:
            print()
            print("❌ Opção inválida. Por favor, tente novamente. ❌")