# 1. Faça um programa que converta uma temperatura em graus
# Fahrenheit para Celsius. A temperatura em Fahrenheit deverá
# ser lida do teclado. Utilize a fórmula C = (F - 32) * 5/9, onde F
# é a temperatura em Fahrenheit e C é a temperatura em
# Celsius.
f = float(input("Digite a temperatura em Fahrenheit: "))
c = (f - 32) * 5/9
print("A temperatura em Celsius é:", c)

# ----------------------------------------------------------------------
# 2. Faça um programa que:
# - Leia a cotação do dólar
# - Leia um valor em dólares
# - Converta esse valor para Real (consulte a cotação atual
# do dólar na Internet)
# - Mostre o resultado
cotacao_dolar = float(input("Digite a cotação do dólar: "))
valor_dolares = float(input("Digite o valor em dólares: "))
valor_reais = valor_dolares * cotacao_dolar
print("O valor em Reais é: R$", valor_reais)

# ----------------------------------------------------------------------
# 3. Leia uma velocidade em km/h (quilômetros por hora) e
# apresente-a convertida em m/s(metros por segundo). A
# fórmula de conversão é: M = K/3.6, sendo K a velocidade
# em km/h e M em m/s.
k = float(input("Digite a velocidade em km/h: "))
m = k / 3.6
print("A velocidade em m/s é:", m)

# ----------------------------------------------------------------------
# 4. Uma empresa contrata um encanador a R$ 30,00 por
# dia. Faça um programa que solicite o número de dias
# trabalhados pelo encanador e imprima a quantia líquida
# que deverá ser paga, sabendo-se que são descontados
# 8% para imposto de renda.
dias_trabalhados = int(input("Digite o número de dias trabalhados: "))
valor_bruto = dias_trabalhados * 30.00
imposto = valor_bruto * 0.08
quantia_liquida = valor_bruto - imposto
# Ou quantia_liquida = valor_bruto * 0.92
print("A quantia líquida a ser paga é: R$", quantia_liquida)

# ----------------------------------------------------------------------
# 5. Receba a altura do degrau de uma escada e a altura que
# o usuário deseja alcançar subindo a escada. Calcule e
# mostre quantos degraus o usuário deverá subir para
# atingir seu objetivo.
altura_degrau = float(input("Digite a altura do degrau (em metros): "))
altura_desejada = float(input("Digite a altura que deseja alcançar (em metros): "))
numero_degraus = altura_desejada / altura_degrau
print("O usuário deverá subir", numero_degraus, "degraus.")

# ----------------------------------------------------------------------
# 6. Determinar a quantidade de litros de combustível gastos em
# uma viagem por um automóvel com autonomia de 12
# km/litro. Para isso, deverá ser informado o tempo gasto na
# viagem e a velocidade média do automóvel. Com esses dados
# será possível calcular a distância percorrida:
# distância = velocidade média * tempo
# e o consumo de combustível usado na viagem:
# consumo = distância / autonomia
# O programa deverá apresentar os seguintes valores:
# velocidade média, tempo gasto na viagem, distância
# percorrida e a quantidade de combustível consumido na
# viagem.
tempo_gasto = float(input("Digite o tempo gasto na viagem (em horas): "))
velocidade_media = float(input("Digite a velocidade média (em km/h): "))

autonomia = 12 # km/litro

distancia_percorrida = velocidade_media * tempo_gasto
combustivel_consumido = distancia_percorrida / autonomia

print("\nResumo da Viagem:")
print("Velocidade média:", velocidade_media, "km/h")
print("Tempo gasto na viagem:", tempo_gasto, "horas")
print("Distância percorrida:", distancia_percorrida, "km")
print("Quantidade de combustível consumido:", combustivel_consumido, "litros")

# ----------------------------------------------------------------------
# 7. Faça um programa para ler as dimensões de um terreno
# (comprimento c e largura l), bem como o preço do
# metro de tela p. Imprima o custo para cercar este
# mesmo terreno com tela.
c_terreno = float(input("Digite o comprimento do terreno (metros): "))
l_terreno = float(input("Digite la largura do terreno (metros): "))
p_tela = float(input("Digite o preço do metro da tela (R$): "))

perimetro = 2 * (c_terreno + l_terreno)
custo_cerca = perimetro * p_tela
print("O custo para cercar o terreno é: R$", custo_cerca)

# ----------------------------------------------------------------------
# 8. Faça um programa que leia um número inteiro positivo
# de três dígitos (de 100 a 999). Gere outro número
# formado pelos dígitos invertidos do número lido.
# Exemplo:
# Número lido: 123
# Número Gerado:321
numero_lido = int(input("Digite um número inteiro de três dígitos (100-999): "))

d1_unidade = numero_lido % 10
parte_restante = numero_lido // 10
d2_dezena = parte_restante % 10
d3_centena = parte_restante // 10

numero_gerado = (d1_unidade * 100) + (d2_dezena * 10) + d3_centena
print("Número lido:", numero_lido)
print("Número gerado (invertido):", numero_gerado)