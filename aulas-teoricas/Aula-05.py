# 1. Qual a saída dos seguintes códigos?

# a) 

# x = 0
# a = 5
# b = 5
# if a > 0:
#     if b < 0:
#         x = x + 5
#     elif a > 5:
#         x = x + 4
#     else:
#         x = x + 3
# else:
#     x = x + 2
# print(x)

saida = 3

# ----------------------------------------------------------------------

# b)

# x = 0
# a = 0
# b = -5
# if a > 0:
#     if b < 0:
#         x = x + 5
#     elif a > 5:
#         x = x + 4
#     else:
#         x = x + 3
# else:
#     x = x + 2
# print(x)

saida = 2

# ----------------------------------------------------------------------

# 3. Faça um Programa que peça um valor e mostre na tela se o
# valor é positivo, negativo ou nulo.

valor = float(input("Digite um valor: "))

if valor > 0:
    print("O valor é positivo")
elif valor < 0:
    print("O valor é negativo")
else:
    print("O valor é nulo")

# ----------------------------------------------------------------------

# 4. Elabora um programa que ao receber um número inteiro
# determine retorne se o mesmo é par ou ímpar.

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")

# ----------------------------------------------------------------------

# 5. Faça um Programa que peça três números e imprima o maior
# deles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

print("O maior número é:", maior)

# ----------------------------------------------------------------------

# 6. Desenvolver um algoritmo que leia um número inteiro e
# verifique se o número é divisível por 5 e por 3 ao mesmo
# tempo.

numero = int(input("Digite um número inteiro: "))

if numero % 5 == 0 and numero % 3 == 0:
    print("O número é divisível por 5 e por 3 ao mesmo tempo")
else:
    print("O número NÃO é divisível por 5 e por 3 ao mesmo tempo")

# ----------------------------------------------------------------------

# 7. Desenvolver um algoritmo para ler um número “x” e calcular
# e imprimir o valor de “y” de acordo com as condições abaixo:
# • y = x , se x < 1;
# • y = 0 , se x = 1;
# • y = x² , se x > 1;  

x = float(input("Digite o valor de x: "))

if x < 1:
    y = x
elif x == 1:
    y = 0
else:
    y = x**2

print("O valor de y é:", y)