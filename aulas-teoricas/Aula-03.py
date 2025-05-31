# 1. Efetue a transformação de binário para decimal ou vice-
# versa

# a) 33
00100001

# b) 18
00010010

# c) 5
00000101

# d) 24
00011000

# e) 00000110
6

# f) 01100100
100

# g) 00011001
25

# h) 00000010
2

# ----------------------------------------------------------------------

# 2. Faça o teste de mesa para os seguintes trechos de programas
# a) x = 36 / 4 * (3 + 2) * 4 + 2

36/4 = 9.0
(3 + 2) = 5
9.0 *5
45.0*4 = 180.0
180.0 +2 = 182.0

x= 182.0

# ----------------------------------------------------------------------

# b)
# valueOne = 5 ** 2
# valueTwo = 5 ** 3

valueOne = 25
valueTwo = 125

# ----------------------------------------------------------------------

# c)
# x = 7
# y = 5
# a = y // x
# b = x % y
# x = x + a
# y = y - b

# print(a, b, x, y)

# 5 // 7 = 0
# 7 % 5 = 2
# 7 + 0 = 7
# 5 - 2 = 3

a= 0
b= 2
x= 7
y= 3

# ----------------------------------------------------------------------

# 3. Sabendo que A=5, B=4 e C=3 e D=6, informe se as
# expressões abaixo são Verdadeiras ou Falsas.
# a) (A > C) and (C <= D)
True

# b) (A+B) > 10 or (A+B) == (C+D)
True

# c) (A>=C) and (D >= C)
True

# ----------------------------------------------------------------------

# 4. Sabendo que A=20, B=0, C=1 e D=10, informe se as
# expressões são Verdadeiras ou Falsas.

# a) (A – B + D) >= C
True

# b) (A > (A + D)) or (C > B)
True

# c) ((A * D) > (C + A)) and (A > B)
True

# d) (((A + B) / C) >= 0,9) and ((B * D) < 0)
False

# e) ((( A + C)/D) > 0,3) and(((B –C)<0) ) or ((C+A) > D)
True

# f) ((( A + C)/D) > 0,3) and (((B –C)<0) or ((C+A) > D))
True

# ----------------------------------------------------------------------

# 5. Suponha que o valor de uma certa variável inteira A=5 e de
# uma Variável B=13, como poderíamos trocar o valor dessas
# variáveis, ou seja, A=13 e B=5?

A=13
B=5

c = A
A = B
B = c

# ----------------------------------------------------------------------

# 6. Faça um programa para receber um número inteiro
# representando segundos e imprimir a quantidade
# correspondente em horas, minutos e segundos.

segundos_total = int(input("Digite o total de segundos: "))

horas = int(segundos_total / 3600)
minutos = int((segundos_total % 3600) / 60)
segundos = int((segundos_total % 3600) % 60)

print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos)

# ----------------------------------------------------------------------

# 7. Construir um programa que leia o salário mensal atual de
# um funcionário e o percentual de reajuste. Determine o
# valor do novo salário e imprima os valores lidos e o novo
# salário.

salario_atual = float(input("Digite o salário atual: R$"))
percentual = float(input("Digite o percentual de reajuste: %"))

novo_salario = salario_atual * (1 + (percentual/100))

print("Salário atual: R$", salario_atual)
print("Percentual de reajuste: %", percentual)
print("Novo salário: R$", novo_salario)

# ----------------------------------------------------------------------

# 8. A loja “FiqueFeliz” resolveu liquidar todos os seus
# produtos, para isso necessita de um programa que ajude
# calcular os novos preços desses produtos. Elabore um
# programa que leia o preço de um produto, o valor do
# desconto (em porcentagem) e calcule o novo preço.
# Imprimir o valor do produto, o desconto e o novo valor.

preco_produto = float(input("Digite o preço do produto: R$"))
percentual_desconto = float(input("Digite o percentual de desconto: %"))

valor_desconto = preco_produto * (percentual_desconto/100)
novo_preco = preco_produto - valor_desconto

print("Valor do produto: R$", preco_produto)
print("Valor do desconto: R$", valor_desconto)
print("Novo valor: R$", novo_preco)

# ----------------------------------------------------------------------

# 9. Escrever um programa que faz a leitura de um número
# inteiro de até 2 dígitos e imprima a soma dos dígitos.
# Considere que somente serão digitados números de 1 ou 2
# dígitos

numero = int(input("Digite um número de até 2 dígitos: "))

if numero < 10:
    soma = numero
else:
    dezena = int(numero / 10)
    unidade = numero % 10
    soma = dezena + unidade

print("Soma dos dígitos: ", soma)

# ----------------------------------------------------------------------

# 10. Uma empresa paga a seus empregados um salário de R$1.500,00 por mês
# mais uma comissão de R$200,00 para cada carro vendido e mais 5% do
# valor da venda. Construir um programa para calcular o salário do mês de
# um funcionário, de acordo com o descrito acima. Para o cálculo da
# comissão e do adicional de 5% do valor da venda, o programa deverá ler o
# número de carros vendidos e valor total das vendas, do empregado, no mês
# e, imprimir de forma bem explicativa o salário do funcionário:

salario_base = 1500.00
comissao_por_carro = 200.00
adicional_vendas = 0.05

carros_vendidos = int(input("Número de carros vendidos: "))
valor_total_vendas = float(input("Valor total das vendas: R$ "))

total_comissao = carros_vendidos * comissao_por_carro
total_adicional = valor_total_vendas * adicional_vendas
salario_final = salario_base + total_comissao + total_adicional

print("\n• Salário Base: R$ 1500.00")
print("• Número de Carros Vendidos:", carros_vendidos)
print("• Total de Vendas: R$", valor_total_vendas)
print("• Total de Comissão: R$", total_comissao)
print("• Total de Adicional de 5%: R$", total_adicional)
print("• Salario a RECEBER: R$", salario_final)