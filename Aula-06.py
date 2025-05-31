# 1. Faça uma pesquisa sobre os métodos remove(), del() e pop().
# Para que servem, qual a diferença entre eles?

# remove(valor): Exclui o primeiro item da lista que possui o valor especificado. Não retorna nada. Gera erro se o valor não existir.

# Exemplo: lista.remove(20)
# del lista[indice]: Apaga o item na posição (índice) informada. Pode apagar fatias (del lista[1:3]). Não retorna o item. Gera erro se o índice for inválido.

# Exemplo: del lista[1]
# pop(indice_opcional): Remove e retorna o item da posição (índice). Se nenhum índice for dado, remove e retorna o último item. Gera erro se o índice for inválido ou a lista estiver vazia.

# Exemplo: item = lista.pop(2) ou ultimo = lista.pop()

# ----------------------------------------------------------------------

# 3. Elabore um programa que leia uma lista de no máximo 20
# elementos inteiros. Em seguida o programa deverá imprimir
# a quantidade de valores múltiplos de 3.

lista_numeros = []
limite_maximo = 20
contador_multiplos = 0

print("Quantos números deseja inserir (no máximo 20)?")
num_elementos = int(input())

if num_elementos > limite_maximo:
    num_elementos = limite_maximo
elif num_elementos < 0:
    num_elementos = 0

print("Digite os números inteiros:")
for i in range(num_elementos):
    print("Digite o elemento", i + 1, ":")
    elemento = int(input())
    lista_numeros.append(elemento)

for numero in lista_numeros:
    if numero % 3 == 0:
        contador_multiplos += 1

print("\nA lista inserida foi:", lista_numeros)
print("Quantidade de valores múltiplos de 3 na lista:", contador_multiplos)

# ----------------------------------------------------------------------
# 4. Elabore um programa que leia um conjunto de vários valores
# inteiros e os coloque em 2 listas conforme forem pares ou
# ímpares (uma lista para números pares e outra lista para
# números ímpares). A leitura dos números é finalizada
# quando um número negativo é lido.

lista_pares = []
lista_impares = []

print("Digite números inteiros (um número negativo para finalizar):")

while True:
    numero_lido = int(input("Digite um número: "))
    if numero_lido < 0:
        break 
    
    if numero_lido % 2 == 0:
        lista_pares.append(numero_lido)
    else:
        lista_impares.append(numero_lido)

print("\nNúmeros Pares:", lista_pares)
print("Números Ímpares:", lista_impares)

# ----------------------------------------------------------------------
# 5. Elabore um programa que leia uma lista de no máximo 10
# elementos reais, o programa deverá imprimir o maior e
# segundo maior elemento e suas respectivas posições na
# lista.

lista_reais = []
limite_max_reais = 10

print("Quantos números reais deseja inserir (no máximo 10)?")
num_reais = int(input())

if num_reais > limite_max_reais:
    num_reais = limite_max_reais
elif num_reais < 0:
    num_reais = 0

if num_reais > 0:
    print("Digite os números reais:")
    for i in range(num_reais):
        print("Digite o elemento", i + 1, ":")
        elemento_real = float(input())
        lista_reais.append(elemento_real)

print("\nLista inserida:", lista_reais)

if num_reais == 0:
    print("A lista está vazia. Não há maior nem segundo maior.")
elif num_reais == 1:
    print("Maior elemento:", lista_reais[0], "na posição 0")
    print("Não há segundo maior elemento pois a lista tem apenas um item.")
else:
    if lista_reais[0] > lista_reais[1]:
        maior1 = lista_reais[0]
        pos1 = 0
        maior2 = lista_reais[1]
        pos2 = 1
    else:
        maior1 = lista_reais[1]
        pos1 = 1
        maior2 = lista_reais[0]
        pos2 = 0

    for i in range(2, num_reais):
        if lista_reais[i] > maior1:
            maior2 = maior1 
            pos2 = pos1
            maior1 = lista_reais[i] 
            pos1 = i
        elif lista_reais[i] > maior2 and lista_reais[i] != maior1: 
            maior2 = lista_reais[i]
            pos2 = i
        elif maior1 == maior2 and lista_reais[i] < maior1 :
             maior2 = lista_reais[i]
             pos2 = i

    print("Maior elemento:", maior1, "na posição", pos1)
    if maior1 == maior2 and num_reais > 1:
        if pos1 != pos2: 
             print("Segundo maior elemento:", maior2, "na posição", pos2, "(valor igual ao maior)")
        else: 
             print("Não há um segundo maior elemento claramente distinto (ou todos os elementos são iguais).")
    else:
        print("Segundo maior elemento:", maior2, "na posição", pos2)

# ----------------------------------------------------------------------
# 6. Foram anotadas as idades e alturas de 30 alunos. Faça um
# Programa que determine quantos alunos com mais de 13
# anos possuem altura inferior à média de altura desses
# alunos.

TOTAL_ALUNOS = 3 
idades = []
alturas = []
soma_alturas = 0
contador_alunos_condicao = 0

print("Digite a idade e altura de", TOTAL_ALUNOS, "alunos:")
for i in range(TOTAL_ALUNOS):
    print("\nAluno", i + 1, ":")
    print("  Idade do aluno", i + 1, ":")
    idade_aluno = int(input())
    print("  Altura do aluno", i + 1, "(em metros, ex: 1.75):")
    altura_aluno = float(input())
    
    if idade_aluno <= 0 or altura_aluno <= 0:
        continue 

    idades.append(idade_aluno)
    alturas.append(altura_aluno)
    soma_alturas += altura_aluno

if TOTAL_ALUNOS > 0 and len(alturas) > 0: 
    media_alturas = soma_alturas / len(alturas)
    print("\nA média de altura da turma é:", media_alturas, "metros")

    for i in range(len(idades)): 
        if idades[i] > 13 and alturas[i] < media_alturas:
            contador_alunos_condicao += 1
    
    print("Número de alunos com mais de 13 anos e altura inferior à média:", contador_alunos_condicao)
else:
    print("Nenhum dado de aluno válido foi inserido.")

# ----------------------------------------------------------------------
# 7. Construa um programa que leia dois números inteiros: a e b
# e uma lista com N valores inteiros (N fornecido pelo usuário).
# O programa deverá imprimir quantos elementos da Lista
# pertencem ao intervalo [a;b].

print("Digite o valor inicial do intervalo (a):")
a = int(input())
print("Digite o valor final do intervalo (b):")
b = int(input())

if a > b:
    temp = a
    a = b
    b = temp

print("Quantos valores inteiros a lista terá (N)?")
n_elementos = int(input())
lista_valores = []
contador_no_intervalo = 0

if n_elementos > 0:
    print("Digite os", n_elementos, "valores da lista:")
    for i in range(n_elementos):
        print("Valor", i + 1, ":")
        valor_lido = int(input())
        lista_valores.append(valor_lido)
    
    for elemento_lista in lista_valores:
        if a <= elemento_lista <= b: 
            contador_no_intervalo += 1
            
    print("\nLista:", lista_valores)
    print("Intervalo: [",a,",",b,"]") 
    print("Número de elementos da lista que pertencem ao intervalo:", contador_no_intervalo)
else:
    print("A lista não terá elementos.")