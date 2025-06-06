# 1. Leia um número inteiro e imprima resultado da diferença do seu
# triplo pelo dobro do seu sucessor.
num = int(input())
sucessor = num + 1
resultado = (num * 3) - (sucessor * 2)
print(resultado)

# ----------------------------------------------------------------------
# 2. Determine a área de um triângulo
base = float(input("Base do triangulo: "))
altura = float(input("Altura do triangulo: "))
area = (base * altura) / 2
print("Área do triangulo: ", area)

# ----------------------------------------------------------------------
# 3. Leia o salário mensal atual de um funcionário e o percentual de
# reajuste e determine o valor do novo salário.
salario_atual = float(input("Salário mensal: R$"))
percentual_reajuste = float(input("Porcentagem de reajuste: %"))
novo_salario = salario_atual * (1 + (percentual_reajuste / 100))
print("Novo salario: R$", novo_salario)

# ----------------------------------------------------------------------
# 4. Calcule o volume do cubo.
aresta = float(input("Valor de uma aresta: "))
volume = aresta ** 3
print("Volume do cubo: ", volume)

# ----------------------------------------------------------------------
# 5. Elabore um programa que dada uma distância percorrida (em
# quilômetros), bem como o total de combustível gasto (em litros),
# informe o consumo do veículo.
km = float(input("Distancia em Km: "))
combustivel = float(input("Combustível gasto em Litros: "))
consumo = km / combustivel
print("Consumo do veículo: ", consumo, "km/L")

# ----------------------------------------------------------------------
# 6. Faça um programa que dadas as medidas de uma sala em metro
# (comprimento e largura), bem como o preço do metro quadrado
# do carpete, informe o custo total para forrar o piso da sala.
comprimento = float(input("Comprimento da sala: "))
largura = float(input("Largura da saala: "))
preco_m2_carpete = float(input("Preço do m2 do carpete: "))
area_sala = comprimento * largura
custo_total = area_sala * preco_m2_carpete
print("Preço total para forrar: R$", custo_total)

# ----------------------------------------------------------------------
# 7. O índice de massa corpórea (IMC) de uma pessoa é igual ao peso
# (em quilogramas) dividido pelo quadrado de sua altura (em
# metros). Construa um programa que dados o peso e altura de
# uma pessoa, informe o valor de seu IMC.
peso = float(input("Seu peso (em kg): "))
altura = float(input("Sua altura (em metros): "))
imc = peso / (altura * altura)
print("IMC: ", imc)

# ----------------------------------------------------------------------
# 8. Uma certa importância será dividida entre três ganhadores de
# um concurso. Sendo que da quantia total:
# • O primeiro ganhador recebera 46%;
# • O segundo recebera 32%;
# • O terceiro recebera o restante;
# Elabore um programa que dado o valor do concurso em reais ele,
# calcule e imprima a quantia ganha por cada um dos ganhadores.
valor_concurso = float(input("Premio total: "))
ganhador1_percentual = 0.46
ganhador2_percentual = 0.32

quantia_ganhador1 = valor_concurso * ganhador1_percentual
quantia_ganhador2 = valor_concurso * ganhador2_percentual
quantia_ganhador3 = valor_concurso - (quantia_ganhador1 + quantia_ganhador2)

print("Primeiro receberá: R$", quantia_ganhador1)
print("Segundo receberá: R$", quantia_ganhador2)
print("Terceiro receberá: R$", quantia_ganhador3)

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

valor_compra = int(input("Digite o Valor da Compra: "))
valor_pago = int(input("Digite o Valor do Pagamento: "))

print("Compra: R$" + str(valor_compra) + ".00")
print("Pagamento: R$" + str(valor_pago) + ".00")

troco = valor_pago - valor_compra
print("Troco: R$" + str(troco) + ".00")

if troco > 0:
    print("EM:")
    
    nota100 = int(troco / 100)
    troco = troco % 100
    print("R$100,00", nota100, "cédulas")
    
    nota50 = int(troco / 50)
    troco = troco % 50
    print("R$ 50,00", nota50, "cédulas")
    
    nota20 = int(troco / 20)
    troco = troco % 20
    print("R$ 20,00", nota20, "cédulas")
    
    nota10 = int(troco / 10)
    troco = troco % 10
    print("R$ 10,00", nota10, "cédulas")
    
    nota5 = int(troco / 5)
    troco = troco % 5
    print("R$  5,00", nota5, "cédulas")
    
    nota1 = int(troco / 1)
    print("R$  1,00", nota1, "cédulas")