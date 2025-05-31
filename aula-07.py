# Seja a seguinte definição de uma estrutura de dados
# representando um livro:
# • código do livro: número inteiro
# • título: string
# • número de autores: número inteiro
# de acordo com o número de autores – nomes dos
# autores: string
# • preço: número real
#
# Você irá trabalhar com dicionários e listas
# Crie um dicionário de livros, onde o código do livro é a chave e
# este dicionário, para cada chave é constituído de uma lista com
# as outras informações (Veja os exemplos acima)
# Na construção do programa use o tratamento de exceções
# Após a leitura dos dados, realizara as seguintes tarefas
# • Buscar um livro pelo título, imprimir todas as suas informações
# se ele existir
# • Buscar um livro pelo código, imprimir todas as suas
# informações se ele existir
# • imprimir os dados dos livros com preço superior a R$50.00.
# Apresente os dados no formato de uma tabela.

livros_db = {} 

def imprimir_dados_livro_simples(codigo, dados_livro):
    titulo = dados_livro[0]
    nomes_autores_lista = dados_livro[2]
    preco = dados_livro[3]
    autores_str = ", ".join(nomes_autores_lista) 
    print(codigo, "|", titulo, "|", autores_str, "| R$", preco)

def imprimir_cabecalho_simples():
    print("Código | Título | Autor(es) | Preço")
    print("------------------------------------------------------------------")

while True:
    print("\n--- Menu Biblioteca ---")
    print("1. Adicionar Novo Livro")
    print("2. Buscar Livro por Título")
    print("3. Buscar Livro por Código")
    print("4. Listar Livros com Preço > R$50.00")
    print("5. Listar Todos os Livros")
    print("6. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("\n--- Adicionar Novo Livro ---")
        try:
            codigo = int(input("Digite o código do livro (número inteiro): "))
            if codigo in livros_db:
                print("Erro: Já existe um livro com este código.")
                continue 

            titulo = input("Digite o título do livro: ")
            
            num_autores = int(input("Digite o número de autores: "))
            if num_autores < 0:
                print("Número de autores não pode ser negativo.")
                continue
            
            nomes_autores = []
            for i in range(num_autores):
                nome_autor = input("Digite o nome do autor " + str(i+1) + ": ")
                nomes_autores.append(nome_autor)
            
            preco = float(input("Digite o preço do livro (ex: 25.99): "))
            if preco < 0:
                print("Preço não pode ser negativo.")
                continue

            livros_db[codigo] = [titulo, num_autores, nomes_autores, preco]
            print("Livro adicionado com sucesso!")

        except ValueError:
            print("Erro: Entrada inválida. Certifique-se de digitar números onde esperado.")
        except Exception as e:
            print("Ocorreu um erro inesperado:", str(e))

    elif opcao == '2':
        print("\n--- Buscar Livro por Título ---")
        if not livros_db:
            print("Nenhum livro cadastrado ainda.")
            continue

        titulo_busca = input("Digite o título do livro a buscar: ")
        encontrado = False
        imprimir_cabecalho_simples()
        for codigo_livro, dados_livro in livros_db.items():
            if titulo_busca.lower() in dados_livro[0].lower(): 
                imprimir_dados_livro_simples(codigo_livro, dados_livro)
                encontrado = True
        if not encontrado:
            print("Nenhum livro encontrado com esse título.")
        print("------------------------------------------------------------------")


    elif opcao == '3':
        print("\n--- Buscar Livro por Código ---")
        if not livros_db:
            print("Nenhum livro cadastrado ainda.")
            continue
        try:
            codigo_busca = int(input("Digite o código do livro a buscar: "))
            if codigo_busca in livros_db:
                imprimir_cabecalho_simples()
                imprimir_dados_livro_simples(codigo_busca, livros_db[codigo_busca])
                print("------------------------------------------------------------------")
            else:
                print("Nenhum livro encontrado com esse código.")
        except ValueError:
            print("Erro: Código deve ser um número inteiro.")

    elif opcao == '4':
        print("\n--- Livros com Preço > R$50.00 ---")
        if not livros_db:
            print("Nenhum livro cadastrado ainda.")
            continue
        
        encontrados_preco_alto = False
        imprimir_cabecalho_simples()
        for codigo_livro, dados_livro in livros_db.items():
            if dados_livro[3] > 50.00:
                imprimir_dados_livro_simples(codigo_livro, dados_livro)
                encontrados_preco_alto = True
        
        if not encontrados_preco_alto:
            print("Nenhum livro encontrado com preço superior a R$50.00.")
        print("------------------------------------------------------------------")

    elif opcao == '5':
        print("\n--- Listar Todos os Livros ---")
        if not livros_db:
            print("Nenhum livro cadastrado ainda.")
        else:
            imprimir_cabecalho_simples()
            for codigo_livro, dados_livro in livros_db.items():
                imprimir_dados_livro_simples(codigo_livro, dados_livro)
            print("------------------------------------------------------------------")

    elif opcao == '6':
        print("Saindo do programa. Até logo!")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")