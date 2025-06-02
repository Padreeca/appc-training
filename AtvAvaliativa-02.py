voos_cadastrados = {}
passageiros_cadastrados = {}


def cadastrar_novo_voo():
    print("\n--- Cadastrar Voo ---")
    
    num_voo = ""
    entrada_ok = 0 
    while entrada_ok == 0:
        num_voo = input("Digite o código do voo: ")
        if len(num_voo) > 0:
            if num_voo not in voos_cadastrados:
                entrada_ok = 1
            else:
                print("Voo já existente")
        else:
            print("não pode ser vazio")
    print("")
    origem_voo = ""
    entrada_ok = 0
    while entrada_ok == 0:
        origem_voo = input("Cidade de origem: ")
        if len(origem_voo) > 2 :
            entrada_ok = 1
        else:
            print("Escreva certo")

    destino_voo = ""
    entrada_ok = 0
    while entrada_ok == 0:
        destino_voo = input("Cidade de destino: ")
        if len(destino_voo) > 2:
            if destino_voo != origem_voo:
                entrada_ok = 1
            else:
                print("Destino não pode ser igual a origem.")
        else:
            print("Escreva certo")

    print("")

    escalas_voo_int = -1
    entrada_ok = 0
    while entrada_ok == 0:
        try:
            escalas_voo_int = int(input("Qauntas escalas?  "))
            if escalas_voo_int >= 0:
                entrada_ok = 1
            else:
                print("Precisa ser 0 ou mais")
        except ValueError:
            print("Digite um numero inteiro")
    print("")
            
    preco_voo_float = -1.0
    entrada_ok = 0
    while entrada_ok == 0:
        try:
            preco_voo_float = float(input("Preço da passagem (ponto para os centavos): "))
            if preco_voo_float > 0:
                entrada_ok = 1
            else:
                print("não pode ser negativo ou zero")
        except ValueError:
            print("Valor inválido. (coloque com ponto)")


    lugares_voo_int = -1
    entrada_ok = 0
    while entrada_ok == 0:
        try:
            lugares_voo_int = int(input("Quantidade de lugares disponíveis: "))
            if lugares_voo_int > 0:
                entrada_ok = 1
            else:
                print("Quantidade de lugares tem que ser maior que zero.")
        except ValueError:
            print("digite um numero inteiro")

    voos_cadastrados[num_voo] = {
        "origem": origem_voo,
        "destino": destino_voo,
        "escalas": escalas_voo_int,
        "preco": preco_voo_float,
        "lugares_disponiveis": lugares_voo_int,
        "passageiros_do_voo": []
    }
    
    print("\n---> Voo", num_voo, "cadastrado com sucesso")
    print("------------------------------------")

def consultar_voo_por_codigo():
    print("\n--- Consultar Voo por Código ---")
    if not voos_cadastrados:
        print("Nenhum voo cadastrado")
        print("------------------------------------")
        return
    codigo_consulta = input("Código do voo: ")
    print("")
    if codigo_consulta in voos_cadastrados:
        detalhes_voo = voos_cadastrados[codigo_consulta]
        print("Detalhes do Voo: ", codigo_consulta)
        print("  Origem: ", detalhes_voo["origem"])
        print("  Destino: ", detalhes_voo["destino"])
        print("  Escalas: ", detalhes_voo["escalas"])
        print("  Preço: R$", detalhes_voo["preco"])
        print("  Lugares Disponíveis: ", detalhes_voo["lugares_disponiveis"])
        print("  Passageiros(CPF): ", detalhes_voo["passageiros_do_voo"])
    else:
        print("Voo ", codigo_consulta, "não encontrado.")
    
    print("------------------------------------")


def consultar_voo_por_origem():
    print("\n--- Consultar por Origem ---")
    if not voos_cadastrados:
        print("Nenhum voo cadastrado.")
        print("------------------------------------")
        return
    origem_consulta = input("Cidade de origem: ")
    print("")
    
    voos_encontrados = 0
    for codigo_voo, detalhes_voo in voos_cadastrados.items():
        if detalhes_voo["origem"].lower() == origem_consulta.lower(): 
            print("Voo:", codigo_voo)
            print("  Destino: ", detalhes_voo["destino"])
            print("  Preço: R$", detalhes_voo["preco"])
            print("")
            voos_encontrados = 1
            
    if voos_encontrados == 0:
        print("Nenhum voo com origem em  ", origem_consulta)
        
    print("------------------------------------")

def consultar_voo_por_destino():
    print("\n--- Consultar por destino ---")
    if not voos_cadastrados:
        print("Nenhum voo cadastrado")
        print("------------------------------------")
        return

    destino_consulta = input("Cidade de destino: ")
    print("")
    voos_encontrados = 0
    for codigo_voo, detalhes_voo in voos_cadastrados.items():
        if detalhes_voo["destino"].lower() == destino_consulta.lower():
            print("Voo:", codigo_voo)
            print("  Origem:", detalhes_voo["origem"])
            print("  Preço: R$", detalhes_voo["preco"])
            print("")
            voos_encontrados = 1

    if voos_encontrados == 0:
        print("Nenhum voo encontrado com destino para", destino_consulta)

    print("------------------------------------")


def consultar_voo_menor_escala():
    print("\n--- Voo com Menor Número de Escalas: ---")
    if not voos_cadastrados:
        print("Nenhum voo cadastrado.")
        print("------------------------------------")
        return

    origem_desejada = input("Cidade de origem: ")
    destino_desejado = input("Cidade destino: ")
    print("")

    voo_escolhido = ""
    menor_num_escalas = -1 
    encontrou_algum_voo = 0
    # print("origem:", origem_desejada, "destino:", destino_desejado)

    for codigo_voo, detalhes_voo in voos_cadastrados.items():
        # print( codigo_voo, "escalas:", detalhes_voo["escalas"])
        if detalhes_voo["origem"].lower() == origem_desejada.lower() and \
           detalhes_voo["destino"].lower() == destino_desejado.lower():
            encontrou_algum_voo = 1
            # print( codigo_voo)
            if menor_num_escalas == -1 or detalhes_voo["escalas"] < menor_num_escalas:
                menor_num_escalas = detalhes_voo["escalas"]
                voo_escolhido = codigo_voo
                # print("Novo menor:", menor_num_escalas, voo_escolhido)
    
    if encontrou_algum_voo == 0:
        print("Nenhum voo de", origem_desejada, "para", destino_desejado)
    elif voo_escolhido != "":
        print("Voo com menor número de escalas de", origem_desejada, "para", destino_desejado, "é:")
        print("  Código do Voo:", voo_escolhido)
        print("  Escalas:", voos_cadastrados[voo_escolhido]["escalas"])
        print("  Preço: R$", voos_cadastrados[voo_escolhido]["preco"])
    else:
        
        print("Não tem voo com menor n° de escala")

    print("------------------------------------")


def consultar_voo():
    opcao_consulta = -1

    while opcao_consulta != 0:
        print("\n--- Consultas de Voos ---")
        print("1. Código do voo")
        print("2. Cidade de origem")
        print("3. Cidade de destino")
        print("4. Voo com menor número de escalas\n")
        print("0. Voltar ao Menu Principal")

        entrada_consulta_ok = 0
        while entrada_consulta_ok == 0:
            try:
                opcao_consulta = int(input("\nEscolha uma opção de consulta: "))
                if 0 <= opcao_consulta <= 4:
                    entrada_consulta_ok = 1
                else:
                    print("\nescolha um número do menu.")
            except ValueError:
                print("\nDigite um número.")
        
        print("")

        if opcao_consulta == 1:
            consultar_voo_por_codigo()
        elif opcao_consulta == 2:
            consultar_voo_por_origem()
        elif opcao_consulta == 3:
            consultar_voo_por_destino()
        elif opcao_consulta == 4:
            consultar_voo_menor_escala()
    print("")

def listar_passageiros_voo():
    print("\n--- Passageiros de um Voo ---")
    if not voos_cadastrados:
        print("Nenhum voo cadastrado")
        print("------------------------------------")
        return

    codigo_voo = input("Qual o códugo do voo? ")
    print("")

    if codigo_voo in voos_cadastrados:
        detalhes_voo = voos_cadastrados[codigo_voo]
        print("Voo: ", codigo_voo)
        print("Origem: ", detalhes_voo["origem"], "- Destino:", detalhes_voo["destino"])
        print("Lugares Disponíveis:", detalhes_voo["lugares_disponiveis"])
        
        lista_cpfs_passageiros = detalhes_voo["passageiros_do_voo"]
        # print(lista_cpfs_passageiros)
        
        if not lista_cpfs_passageiros:
            print("Nenhum passageiro neste voo.")
        else:
            print("\nPassageiros no voo:")
            for cpf in lista_cpfs_passageiros:
                if cpf in passageiros_cadastrados:
                    info_passageiro = passageiros_cadastrados[cpf]
                    print("  CPF:", cpf, "- Nome:", info_passageiro["nome"], "- Telefone:", info_passageiro["telefone"])
                else:
                    print("  CPF:", cpf, "- (Dados do passageiro não encontrados no cadastro geral)")
    else:
        print("Voo ", codigo_voo, "não encontrado")
        
    print("------------------------------------")

def vender_passagem():
    print("\n--- Venda de Passagem ---")
    if not voos_cadastrados:
        print("NEnhum voo cadastrado")
        print("------------------------------------")
        return

    codigo_voo_venda = input("Qual o código do voo? ")
    print("")

    if codigo_voo_venda not in voos_cadastrados:
        print("Voo", codigo_voo_venda, "não existe.")
        print("------------------------------------")
        return

    detalhes_voo_venda = voos_cadastrados[codigo_voo_venda]
    # print(detalhes_voo_venda)

    if detalhes_voo_venda["lugares_disponiveis"] == 0:
        print("Voo ", codigo_voo_venda, "está lotado.")
        print("------------------------------------")
        return
        
    print("Voo selecionado: ", codigo_voo_venda)
    print("Origem:", detalhes_voo_venda["origem"], "- Destino:", detalhes_voo_venda["destino"])
    print("Preço: R$", detalhes_voo_venda["preco"])
    print("Lugares disponíveis: ", detalhes_voo_venda["lugares_disponiveis"])
    print("")

    cpf_passageiro = ""
    entrada_ok = 0
    while entrada_ok == 0:
        cpf_passageiro = input("CPF do passageiro: ")
        if cpf_passageiro.isdigit() and len(cpf_passageiro) == 11 :
            entrada_ok = 1
        else:
            print("CPF tem 11 numeros.")

    nome_passageiro = ""
    telefone_passageiro = ""

    if cpf_passageiro in passageiros_cadastrados:
        print("Passageiro já existe")
        nome_passageiro_cadastrado = passageiros_cadastrados[cpf_passageiro]["nome"]
        
        nome_novo = input(f"nome do passageiro ({nome_passageiro_cadastrado}): ") or nome_passageiro_cadastrado
        if nome_novo.strip().lower() != nome_passageiro_cadastrado.lower() and nome_novo.strip() != "": 
             print("Nome diferente do cadastrado")
             passageiros_cadastrados[cpf_passageiro]["nome"] = nome_novo.strip()
        
        nome_passageiro = passageiros_cadastrados[cpf_passageiro]["nome"]
        telefone_passageiro = passageiros_cadastrados[cpf_passageiro]["telefone"] 
        print("Nome:", nome_passageiro, "- Telefone:", telefone_passageiro)
        # print("nome_passageiro)

    else:
        print("Novo passageiro: ")
        entrada_ok = 0
        while entrada_ok == 0:
            nome_passageiro = input("nome completo do passageiro: ")
            if len(nome_passageiro) > 3: 
                entrada_ok = 1
            else:
                print("digite certo")
        
        entrada_ok = 0
        while entrada_ok == 0:
            telefone_passageiro = input("telefone: ")
            if telefone_passageiro.isdigit() and len(telefone_passageiro) >= 8: 
                 entrada_ok = 1
            else:
                print("Telefone inválido.")
        
        passageiros_cadastrados[cpf_passageiro] = {
            "nome": nome_passageiro,
            "telefone": telefone_passageiro
        }
        # print(cpf_passageiro )
        print("Passageiro cadastrado com sucesso.")

    if cpf_passageiro in detalhes_voo_venda["passageiros_do_voo"]:
        print("Passageiro já tem essa passagem")
        print("------------------------------------")
        return

    confirmacao_ok = 0
    while confirmacao_ok == 0:
        confirmar_compra = input(f"Confirmar compra  {codigo_voo_venda} para {nome_passageiro} (CPF: {cpf_passageiro}) por R$ {detalhes_voo_venda['preco']}? (s ou n): ")
        if confirmar_compra.lower() == 's':
            detalhes_voo_venda["lugares_disponiveis"] -= 1
            detalhes_voo_venda["passageiros_do_voo"].append(cpf_passageiro)
            # print( detalhes_voo_venda["lugares_disponiveis"])
            print("\nComprado com sucesso. voo:", codigo_voo_venda)
            confirmacao_ok = 1
        elif confirmar_compra.lower() == 'n':
            print("cancelado")
            confirmacao_ok = 1
        else:
            print("apenas s ou n")

    print("------------------------------------")



def cancelar_passagem():
    print("\n--- Cancelamentos ---")

    if not voos_cadastrados:
        print("Nenhum voo cadastrado ")
        print("------------------------------------")
        return

    codigo_voo_cancelar = input("Codigo do voo: ")
    print("")

    if codigo_voo_cancelar not in voos_cadastrados:
        print("Voo", codigo_voo_cancelar, "não existe.")
        print("------------------------------------")
        return
        
    detalhes_voo_canc = voos_cadastrados[codigo_voo_cancelar]

    if not detalhes_voo_canc["passageiros_do_voo"]:
        print("ainda não tem passageiros para esse voo")
        print("------------------------------------")
        return

    cpf_passageiro_cancelar = ""
    entrada_ok = 0
    while entrada_ok == 0:
        cpf_passageiro_cancelar = input("CPF: ")
        if cpf_passageiro_cancelar.isdigit() and len(cpf_passageiro_cancelar) == 11:
            entrada_ok = 1
        else:
            print("CPF deve ter 11 numeros")
    print("")
    # print(cpf_passageiro_cancelar, codigo_voo_cancelar)
    
    if cpf_passageiro_cancelar not in passageiros_cadastrados:
        print("Passageiro com CPF", cpf_passageiro_cancelar, "não encontrado.")
        
    if cpf_passageiro_cancelar in detalhes_voo_canc["passageiros_do_voo"]:
        confirmacao_ok = 0
        while confirmacao_ok == 0:
            nome_passageiro_display = "desconhecido"
            if cpf_passageiro_cancelar in passageiros_cadastrados:
                nome_passageiro_display = passageiros_cadastrados[cpf_passageiro_cancelar]["nome"]

            confirma = input(f"Confirmar cancelamento da passagem para {nome_passageiro_display} (CPF: {cpf_passageiro_cancelar}) no voo {codigo_voo_cancelar}? (S ou N): ")
            if confirma.lower() == 's':
                detalhes_voo_canc["passageiros_do_voo"].remove(cpf_passageiro_cancelar)
                detalhes_voo_canc["lugares_disponiveis"] += 1
                # print( detalhes_voo_canc["lugares_disponiveis"])
                print("Passagem cancelada")
                confirmacao_ok = 1
            elif confirma.lower() == 'n':
                print("cancelamento não efetuado.")
                confirmacao_ok = 1
            else:
                print("digite s ou n")
    else:
        print("Passageiro com CPF", cpf_passageiro_cancelar, "não possui passagem pra esse voo.")

    print("------------------------------------")


print("Vendas Aéreas")

opcao_escolhida = -1

while opcao_escolhida != 0:
    print("\n--- Menu Principal ---")
    print("1. Cadastrar Novo Voo")
    print("2. Consultar Voo")
    print("3. Listar Passageiros de um Voo")
    print("4. Vender Passagem")
    print("5. Cancelar Passagem")
    print("6. Ver Voos Cadastrados")
    print("7. Ver Passageiros Cadastrados")
    print("\n0. Sair do Sistema")
    print("------------------------------------")

    entrada_menu_ok = 0 
    while entrada_menu_ok == 0:
        try:
            opcao_escolhida = int(input("\nEscolha uma opção: "))
            if 0 <= opcao_escolhida <= 7: 
                entrada_menu_ok = 1
            else:
                print("Escolha um numero do menu")
        except ValueError:
            print("Escolha um numero do menu")
    
    print("")

    if opcao_escolhida == 1:
        cadastrar_novo_voo()
    elif opcao_escolhida == 2:
        consultar_voo()
    elif opcao_escolhida == 3:
        listar_passageiros_voo()
    elif opcao_escolhida == 4:
        vender_passagem()
    elif opcao_escolhida == 5:
        cancelar_passagem()
    elif opcao_escolhida == 6:
        print("\n--- Voos Cadastrados ---")
        if not voos_cadastrados:
            print("Nenhum voo cadastrado")
        else:
            for voo_id, detalhes_voo in voos_cadastrados.items():
                print("")
                print("Voo:", voo_id)
                print("  Origem: ", detalhes_voo["origem"])
                print("  Destino:", detalhes_voo["destino"])
                print("  Escalas: ", detalhes_voo["escalas"])
                print("  Preço: R$", detalhes_voo["preco"])
                print("  Lugares Disponíveis:", detalhes_voo["lugares_disponiveis"])
                print("  Passageiros : ", detalhes_voo["passageiros_do_voo"])
        print("------------------------------------")
    elif opcao_escolhida == 7:
        print("\n--- Passageiros Cadastrados ---")
        if not passageiros_cadastrados:
            print("Nenhum passageiro cadastrado ainda.")
        else:
            for cpf_pass, info_pass in passageiros_cadastrados.items():
                print("")
                print("CPF:", cpf_pass)
                print("  Nome:", info_pass["nome"])
                print("  Telefone:", info_pass["telefone"])
        print("------------------------------------")
    elif opcao_escolhida == 0:
        print("\nSaindo do sistema...")