# 1. Elabore um programa que leia um número inteiro e imprima se ele
# é par ou ímpar
num = int(input("Digite um número: "))
if num % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")

# ----------------------------------------------------------------------

# 2. Construa um programa que leia os lados de um quadrilátero e
# determine se é um Quadrado ou um Retângulo
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))
lado4 = float(input("Digite o quarto lado: "))

if lado1 == lado2 == lado3 == lado4:
    print("É um Quadrado")
else:
    print("É um Retângulo")

# ----------------------------------------------------------------------

# 3. Faça um Programa que peça dois números e imprima o maior deles
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print("O maior número é:", num1)
else:
    print("O maior número é:", num2)

# ----------------------------------------------------------------------

# 4. Faça um Programa que peça um valor e mostre na tela se o valor é
# positivo, negativo ou nulo
valor = float(input("Digite um valor: "))

if valor > 0:
    print("O valor é positivo")
elif valor < 0:
    print("O valor é negativo")
else:
    print("O valor é nulo")

# ----------------------------------------------------------------------

# 5. Crie um algoritmo que receba do usuário um número qualquer e
# verifique se esse é múltiplo de 5
num = int(input("Digite um número: "))

if num % 5 == 0:
    print("O número é múltiplo de 5")
else:
    print("O número não é múltiplo de 5")

# ----------------------------------------------------------------------

# 6. Construir um programa que faz a leitura de dois valores inteiros A e
# B. Se os valores forem iguais deverá somar os dois, caso contrário
# multiplique A por B. Ao final de qualquer um dos cálculos deve-se
# atribuir o resultado para uma variável C e mostrar seu conteúdo na
# tela
A = int(input("Digite o valor A: "))
B = int(input("Digite o valor B: "))

if A == B:
    C = A + B
else:
    C = A * B

print("Resultado C:", C)

# ----------------------------------------------------------------------

# 1. Um funcionário irá receber um aumento de acordo com o seu
# plano de trabalho, de acordo com a tabela:
# Plano 1 = 10%, Plano 2 = 15%, Plano 3 = 20%
# Faça um programa que leia o plano de trabalho e o salário atual de
# um funcionário e calcula e imprime o seu novo salário
plano = int(input("Digite o plano de trabalho (1, 2 ou 3): "))
salario = float(input("Digite o salário atual: R$"))

if plano == 1:
    novo_salario = salario + (salario * 0.10)
elif plano == 2:
    novo_salario = salario + (salario * 0.15)
elif plano == 3:
    novo_salario = salario + (salario * 0.20)

print("Novo salário: R$", novo_salario)

# ----------------------------------------------------------------------

# 2. Escreva um programa que calcule x elevado a n. Considere que n é um
# valor inteiro não negativo. PROIBIDO USAR QUALQUER FUNÇÃO
# MATEMATICA EXISTENTE no PYTHON, incluindo **
x = int(input("Digite o valor de x: "))
n = int(input("Digite o valor de n: "))

resultado = 1
contador = 0

while contador < n:
    resultado = resultado * x
    contador = contador + 1

print("Resultado:", resultado)

# ----------------------------------------------------------------------

# 3. Faça um programa que imprima os números inteiros de 100 a
# 450, que são múltiplos de 7
print("Múltiplos de 7 entre 100 e 450:")
num = 100

while num <= 450:
    if num % 7 == 0:
        print(num)
    num = num + 1

# ----------------------------------------------------------------------

# 4. Escreva um algoritmo que leia n de números inseridos pelo
# usuário (n é fornecido pelo usuário) e realize a soma dos números
# pares e conta quantos impares o usuário digitou. O resultado da
# soma dos pares e o número de ímpares digitados deverá ser
# impresso no final
n = int(input("Quantos números você vai digitar? "))

soma_pares = 0
conta_impares = 0
contador = 0

while contador < n:
    num = int(input("Digite um número: "))
    
    if num % 2 == 0:
        soma_pares = soma_pares + num
    else:
        conta_impares = conta_impares + 1
    
    contador = contador + 1

print("Soma dos números pares:", soma_pares)
print("Quantidade de números ímpares:", conta_impares)