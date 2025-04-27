# Cadastro de notas para Algoritmos de Programação, Projetos e Computação

# Lista para armazenar os dados de todos os alunos
alunos = []

# Solicitar quantidade de alunos
input_ok = 0
while input_ok == 0:
    try:
        qtd_alunos = int(input("\nQuantos alunos serão cadastrados? "))
        if qtd_alunos > 0:
            input_ok = 1
        else:
            print("Digite um número maior que zero!")
    except:
        print("Digite apenas números!")

# Cadastro dos alunos
for i in range(qtd_alunos):
    print(f"\n----------- Cadastro do {i+1}º Aluno -----------")
    
    # Nome do aluno
    nome = input("Nome do aluno: ")
    
    # Notas teóricas
    notas_teoricas = []
    for j in range(2):
        nota_ok = 0
        while nota_ok == 0:
            try:
                nota = float(input(f"Nota da prova teórica T{j+1}: "))
                if 0 <= nota <= 10:
                    notas_teoricas.append(nota)
                    nota_ok = 1
                else:
                    print("A nota deve estar entre 0 e 10!")
            except:
                print("Digite um número válido!")
    
    # Notas práticas
    notas_praticas = []
    for j in range(2):
        nota_ok = 0
        while nota_ok == 0:
            try:
                nota = float(input(f"Nota do projeto P{j+1}: "))
                if 0 <= nota <= 10:
                    notas_praticas.append(nota)
                    nota_ok = 1
                else:
                    print("A nota deve estar entre 0 e 10!")
            except:
                print("Digite um número válido!")
    
    # Cálculo da média teórica: MT = 0,4*T1 + 0,6*T2
    mt = 0.4 * notas_teoricas[0] + 0.6 * notas_teoricas[1]
    
    # Cálculo da média prática: MP = (P1 + P2) / 2
    mp = (notas_praticas[0] + notas_praticas[1]) / 2
    
    # Cálculo da média final baseado nas condições
    if mt >= 5.0 and mp >= 5.0:
        mf = 0.3 * mp + 0.7 * mt
    else:
        # Média final é a menor entre MT e MP
        if mt < mp:
            mf = mt
        else:
            mf = mp
    
    # Adicionar aluno à lista no formato [nome, [T1,T2], [P1,P2], [MT,MP], MF]
    aluno = [nome, notas_teoricas, notas_praticas, [mt, mp], mf]
    alunos.append(aluno)
    
    print(f"Aluno {nome} cadastrado com sucesso!")

# Menu de opções
rodando = 1
while rodando == 1:
    print("\n" + "=====================================================")
    print("MENU DE OPÇÕES")
    print("\n")
    print("1. Mostrar boletim de todos os alunos")
    print("2. Buscar informações de um aluno")
    print("3. Mostrar aluno com maior média final")
    print("4. Mostrar aluno com menor média final")
    print("5. Mostrar percentual de alunos aprovados")
    print("0. Sair do programa")
    
    opcao_ok = 0
    while opcao_ok == 0:
        try:
            opcao = int(input("\nEscolha uma opção: "))
            opcao_ok = 1
        except:
            print("Digite apenas números!")
    
    if opcao == 1:
        # Mostrar boletim de todos os alunos
        print("\n===== BOLETIM GERAL =====")
        print("Nome           MT    MP    MF")
        print("==============================================")
        
        for aluno in alunos:
            nome = aluno[0]
            mt = aluno[3][0]
            mp = aluno[3][1]
            mf = aluno[4]
            
            print(f"{nome:<15} {mt:.1f}  {mp:.1f}  {mf:.1f}")
    
    elif opcao == 2:
        # Buscar informações de um aluno
        nome_busca = input("\nDigite o nome do aluno: ")
        encontrado = 0
        
        for aluno in alunos:
            if aluno[0].lower() == nome_busca.lower():
                print(f"\n===== INFORMAÇÕES DO ALUNO =====")
                print(f"Nome: {aluno[0]}")
                print(f"Notas Teóricas (T1, T2): {aluno[1][0]}, {aluno[1][1]}")
                print(f"Notas Práticas (P1, P2): {aluno[2][0]}, {aluno[2][1]}")
                print(f"Média Teórica (MT): {aluno[3][0]:.1f}")
                print(f"Média Prática (MP): {aluno[3][1]:.1f}")
                print(f"Média Final (MF): {aluno[4]:.1f}")
                encontrado = 1
                break
        
        if encontrado == 0:
            print("\nAluno não encontrado!")
    
    elif opcao == 3:
        # Mostrar aluno com maior média final
        if len(alunos) > 0:
            maior_mf = -1
            aluno_maior = ""
            
            for aluno in alunos:
                if aluno[4] > maior_mf:
                    maior_mf = aluno[4]
                    aluno_maior = aluno[0]
            
            print(f"\nAluno com maior média final: {aluno_maior} (MF = {maior_mf:.1f})")
        else:
            print("\nNenhum aluno cadastrado!")
    
    elif opcao == 4:
        # Mostrar aluno com menor média final
        if len(alunos) > 0:
            menor_mf = 999999  # Um número muito grande como início
            aluno_menor = ""
            
            for aluno in alunos:
                if aluno[4] < menor_mf:
                    menor_mf = aluno[4]
                    aluno_menor = aluno[0]
            
            print(f"\nAluno com menor média final: {aluno_menor} (MF = {menor_mf:.1f})")
        else:
            print("\nNenhum aluno cadastrado!")
    
    elif opcao == 5:
        # Mostrar percentual de alunos aprovados
        if len(alunos) > 0:
            total_alunos = len(alunos)
            aprovados = 0
            
            for aluno in alunos:
                if aluno[4] >= 5.0:
                    aprovados += 1
            
            percentual = (aprovados / total_alunos) * 100
            print(f"\nPercentual de alunos com média final superior a 5.0: {percentual:.1f}%")
        else:
            print("\nNenhum aluno cadastrado!")
    
    elif opcao == 0:
        print("\nEncerrando o programa...")
        rodando = 0
    
    else:
        print("\nOpção inválida! Tente novamente.")