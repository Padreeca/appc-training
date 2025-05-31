# 1. Escrever um algoritmo que leia uma quantidade desconhecida de
# números e conte quantos deles estão nos seguintes intervalos:
# [0,25], [26,50], [51,75] e [76,100]. A entrada de dados deve
# terminar quando for lido um número negativo
intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0

while True:
    num = int(input("Digite um número: "))
    if num < 0:
        break
    
    if num >= 0 and num <= 25:
        intervalo1 = intervalo1 + 1
    elif num >= 26 and num <= 50:
        intervalo2 = intervalo2 + 1
    elif num >= 51 and num <= 75:
        intervalo3 = intervalo3 + 1
    elif num >= 76 and num <= 100:
        intervalo4 = intervalo4 + 1

print("Intervalo [0,25]:", intervalo1)
print("Intervalo [26,50]:", intervalo2)
print("Intervalo [51,75]:", intervalo3)
print("Intervalo [76,100]:", intervalo4)

# ----------------------------------------------------------------------

# 2. Elabore um programa que leia um número e imprima todos os
# números divisíveis por 4 que sejam menores que este número lido
num = int(input("Digite um número: "))
i = 1

print("Números divisíveis por 4 menores que", num, ":")
while i < num:
    if i % 4 == 0:
        print(i)
    i = i + 1

# ----------------------------------------------------------------------

# 3. Escreva um que solicita 10 números ao usuário, e ao final mostre
# os dois maiores números digitados pelo usuário
maior1 = 0
maior2 = 0
contador = 0

while contador < 10:
    num = int(input("Digite um número: "))
    
    if num > maior1:
        maior2 = maior1
        maior1 = num
    elif num > maior2:
        maior2 = num
    
    contador = contador + 1

print("Primeiro maior:", maior1)
print("Segundo maior:", maior2)

# ----------------------------------------------------------------------

# 4. Escreva um programa que, utilizando a fórmula que converte um
# grau Fahrenheit em Celsius, imprime uma tabela com graus em
# Fahrenheit e Celsius, iniciando no grau 30 oF até 50 oF, de 2 em 2
# graus. Pesquise a fórmula na Internet
print("Fahrenheit | Celsius")
fahrenheit = 30

while fahrenheit <= 50:
    celsius = (fahrenheit - 32) * 5 / 9
    print(fahrenheit, "      |", celsius)
    fahrenheit = fahrenheit + 2

# ----------------------------------------------------------------------

# 5. Escreva um programa que calcule e imprima o valor de S:
# S = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50
S = 0
numerador = 1
denominador = 1

while numerador <= 99:
    S = S + (numerador / denominador)
    numerador = numerador + 2
    denominador = denominador + 1

print("Valor de S:", S)

# ----------------------------------------------------------------------

# 6. Escreva um programa que calcule e imprima o valor de S:
# S = 1/1 - 2/4 + 3/9 - 4/16 + ... - 10/100
S = 0
i = 1

while i <= 10:
    termo = i / (i * i)
    if i % 2 == 0:
        S = S - termo
    else:
        S = S + termo
    i = i + 1

print("Valor de S:", S)

# ----------------------------------------------------------------------

# 7. Faça um algoritmo que leia uma quantidade não
# determinada de números positivos. Calcule a quantidade
# de números pares e ímpares, a média de valores pares e a
# média geral dos números lidos. O número que encerrará a
# leitura será zero
pares = 0
impares = 0
soma_pares = 0
soma_total = 0
total_numeros = 0

while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break
    
    total_numeros = total_numeros + 1
    soma_total = soma_total + num
    
    if num % 2 == 0:
        pares = pares + 1
        soma_pares = soma_pares + num
    else:
        impares = impares + 1

if pares > 0:
    media_pares = soma_pares / pares
else:
    media_pares = 0

media_geral = soma_total / total_numeros

print("Quantidade de pares:", pares)
print("Quantidade de ímpares:", impares)
print("Média dos pares:", media_pares)
print("Média geral:", media_geral)

# ----------------------------------------------------------------------

# 8. Dada a sequência matemática de números 2, 3, 5, 8, 13, 21....
# Construa um programa que calcule a soma desta sequência
# para os N primeiros termo onde, N é fornecido pelo usuário
N = int(input("Digite o valor de N: "))

if N >= 1:
    a = 2
    b = 3
    soma = a
    contador = 1
    
    if N >= 2:
        soma = soma + b
        contador = 2
    
    while contador < N:
        proximo = a + b
        soma = soma + proximo
        a = b
        b = proximo
        contador = contador + 1
    
    print("Soma dos", N, "primeiros termos:", soma)

# ----------------------------------------------------------------------

# 9. A prefeitura de uma cidade fez uma pesquisa entre seus
# habitantes, coletando dados sobre o salário e número de
# filhos. A prefeitura deseja saber:
# a. média do salário da população;
# b. média do número de filhos;
# c. maior salário;
# d. percentual de pessoas com salário até R$100,00
soma_salarios = 0
soma_filhos = 0
maior_salario = 0
ate_100 = 0
total_pessoas = 0

while True:
    salario = float(input("Digite o salário (0 para parar): "))
    if salario == 0:
        break
    
    filhos = int(input("Digite o número de filhos: "))
    
    total_pessoas = total_pessoas + 1
    soma_salarios = soma_salarios + salario
    soma_filhos = soma_filhos + filhos
    
    if salario > maior_salario:
        maior_salario = salario
    
    if salario <= 100:
        ate_100 = ate_100 + 1

media_salario = soma_salarios / total_pessoas
media_filhos = soma_filhos / total_pessoas
percentual_100 = (ate_100 / total_pessoas) * 100

print("Média do salário:", media_salario)
print("Média do número de filhos:", media_filhos)
print("Maior salário:", maior_salario)
print("Percentual com salário até R$100:", percentual_100, "%")

# ----------------------------------------------------------------------

# 10. Elabore um programa que leia vários números inteiros, até
# o usuário digitar um número negativo. Para cada número
# lido deverá ser calculado e impresso seu fatorial
while True:
    num = int(input("Digite um número: "))
    if num < 0:
        break
    
    fatorial = 1
    i = 1
    
    while i <= num:
        fatorial = fatorial * i
        i = i + 1
    
    print("Fatorial de", num, "é:", fatorial)

# ----------------------------------------------------------------------

# 11. Faça um programa que receba a idade, altura e peso de 25
# pessoas. Calcule e mostre:
# a. A quantidade de pessoas com idade superior a 50 anos
# b. A média das alturas das pessoas com idade entre 10 e 20 anos
# c. O percentual de pessoas com peso inferior a 50 quilos
acima_50 = 0
soma_alturas_10_20 = 0
pessoas_10_20 = 0
peso_abaixo_50 = 0
contador = 0

while contador < 25:
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))
    peso = float(input("Digite o peso: "))
    
    if idade > 50:
        acima_50 = acima_50 + 1
    
    if idade >= 10 and idade <= 20:
        soma_alturas_10_20 = soma_alturas_10_20 + altura
        pessoas_10_20 = pessoas_10_20 + 1
    
    if peso < 50:
        peso_abaixo_50 = peso_abaixo_50 + 1
    
    contador = contador + 1

if pessoas_10_20 > 0:
    media_alturas = soma_alturas_10_20 / pessoas_10_20
else:
    media_alturas = 0

percentual_peso = (peso_abaixo_50 / 25) * 100

print("Pessoas com idade superior a 50 anos:", acima_50)
print("Média das alturas (10-20 anos):", media_alturas)
print("Percentual com peso inferior a 50kg:", percentual_peso, "%")

# ----------------------------------------------------------------------

# 12. Implemente um programa que determine se um inteiro e
# positivo dado pelo usuário, é primo
num = int(input("Digite um número positivo: "))

if num <= 1:
    print("Não é primo")
else:
    primo = True
    i = 2
    
    while i < num:
        if num % i == 0:
            primo = False
            break
        i = i + 1
    
    if primo:
        print("É primo")
    else:
        print("Não é primo")