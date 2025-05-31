# 1. Elabore um programa que leia um número inteiro e
# imprima o seu antecessor e o seu sucessor

num = int(input("Digite um número: "))
print("Antecessor:", num-1)
print("Sucessor",num+1)

# ------------------------------------------------------
# 2. Elabore um programa que dado o lado de um quadrado
# determine a sua área e seu perímetro

lado = float(input("Digite o lado do quadrado: "))
print("Área do quadrado: ", lado*lado)
print("Perímetro do quadrado: ", lado*4)

# -------------------------------------------------------
# 3. Elabore um programa que imprima a parte inteira e o
# resto da divisão de dois números inteiros
# Exemplo
# 7 ÷ 3
# Parte inteira = 2
# Resto = 1
# Python

numerador = int(input("Numerador: "))
denominador = int(input("Denominador: "))

print("Parte inteira: ", int(numerador/denominador))
print("Resto: ", numerador%denominador)