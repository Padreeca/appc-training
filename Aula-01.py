# 1. Leia um número inteiro e imprima resultado da diferença do seu
# triplo pelo dobro do seu sucessor

num = int(input())
sucessor = num+1
print((num*3)-(sucessor*2))

# ----------------------------------------------------------------------

# 2. Determine a área de um triângulo
base = int(input("Base do triangulo: "))
altura = int(input("Altura do triagnulo: "))

area = ((base*altura)/2)

print("Área do triangulo: ", area)

# ----------------------------------------------------------------------

# 3. Leia o salário mensal atual de um funcionário e o percentual de
# reajuste e determine o valor do novo salário.

salario = float(input("Salário mensal: R$"))
reajuste = float(input("Porcentagem de reajuste: %"))

print("Novo salario: R$",salario*(1+(reajuste/100)))

# ----------------------------------------------------------------------

# 4. Calcule o volume do cubo

aresta = float(input("Valor de uma aresta: "))

print("Volume do cubo: ", aresta**3)

# ----------------------------------------------------------------------

# 5. Elabore um programa que dada uma distância percorrida (em
# quilômetros), bem como o total de combustível gasto (em litros),
# informe o consumo do veículo.

km = float(input("Distancia em Km: "))
combustivel = float(input("Combustível gasto em Litros: "))

print("Consumo do veículo: ", (km/combustivel),"km/L")

# ----------------------------------------------------------------------

# 6. Faça um programa que dadas as medidas de uma sala em metro
# (comprimento e largura), bem como o preço do metro quadrado
# do carpete, informe o custo total para forrar o piso da sala.

comprimento = float(input("Comprimento da sala: "))
largura = float(input("Largura da saala: "))
carpete = float(input("Preço do m2 do carpete: "))

print("Preço total para forrar: R$",((comprimento*largura)*carpete))

# ----------------------------------------------------------------------

# 7. O índice de massa corpórea (IMC) de uma pessoa é igual ao peso
# (em quilogramas) dividido pelo quadrado de sua altura (em
# metros). Construa um programa que dados o peso e altura de
# uma pessoa, informe o valor de seu IMC.

peso = float(input("Seu peso (em kg): "))
altura = float(input("Sua altura (em metros): "))

print("IMC: ", peso/(altura*altura))

# ----------------------------------------------------------------------

# 8. Uma certa importância será dividida entre três ganhadores de
# um concurso. Sendo que da quantia total:
# • O primeiro ganhador recebera 46%;
# • O segundo recebera 32%;
# • O terceiro recebera o restante;   -  22%
# Elabore um programa que dado o valor do concurso em reais ele,
# calcule e imprima a quantia ganha por cada um dos ganhadores.

primeiro = 0.46
segundo = 0.32

premio = float(input("Premio total: "))

print("Primeiro receberá: R$", premio*primeiro)
print("Segudno receberá: R$", premio*segundo)
print("Terceiro receberá: R$", (premio-((premio*primeiro)+(premio*segundo))))

# ----------------------------------------------------------------------

# 9. Elabore um programa que faça a simulação de um caixa
# de uma loja.
# O usuário deverá digitar o Valor da Compra, o Valor Pago
# pelo cliente.
# O programa irá retornar o valor do troco, as cédulas que
# fazem parte do troco e a quantidade de cada cédula.
# Para este programa considere as cédulas de R$100,
# R$50, R$20, R$10, R$5 e R$1 real
# Considere a possibilidade de não haver troco

valor = int(input("Valor da compra: R$"))
pago = int(input("Valor pago: R$"))

troco = pago-valor

print("Troco: R$", troco)

#primeiro é =+ para atribuir antes
cem = int(troco/100)
print("Notas de 100: ",cem)
entregou =+ cem*100

cinquenta = int((troco-entregou)/50)
print("Notas de 50: ",cinquenta)
entregou += cinquenta*50

vinte = int((troco-entregou)/20)
print("Notas de 20: ",vinte)
entregou += vinte*20

dez = int((troco-entregou)/10)
print("Notas de 10: ",dez)
entregou += dez*10

cinco = int((troco-entregou)/5)
print("Notas de 5: ",cinco)
entregou += cinco*5

um = int((troco-entregou)/1)
print("Notas de 1: ",um)
entregou += um*1

print("\nEntregou de troco: R$", entregou)