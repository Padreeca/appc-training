# 1. Faça um programa que solicite o nome do usuário e
# imprima-o na vertical
nome = input("Digite seu nome: ")

for letra in nome:
    print(letra)

# ----------------------------------------------------------------------

# 2. Faça um programa que leia um nome e imprima as 4
# primeiras letras do nome
nome = input("Digite um nome: ")

contador = 0
resultado = ""
for letra in nome:
    if contador < 4:
        resultado = resultado + letra
        contador = contador + 1

print(resultado)

# ----------------------------------------------------------------------

# 3. Elabore um programa que leia nome, sexo e idade de um
# usuário. Se sexo for feminino e idade menor que 25,
# imprime o nome da pessoa e a palavra "ACEITA", caso
# contrário imprimir "NÃO ACEITA"
nome = input("Digite o nome: ")
sexo = input("Digite o sexo (F/M): ")
idade = int(input("Digite a idade: "))

if sexo == "F" and idade < 25:
    print(nome, "ACEITA")
else:
    print("NÃO ACEITA")

# ----------------------------------------------------------------------

# 4. Construa um programa que leia duas strings fornecidas pelo
# usuário e verifique se a segunda string lida está contida no
# final da primeira, imprimindo o resultado da verificação
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

if string1.endswith(string2):
    print("A segunda string está no final da primeira")
else:
    print("A segunda string não está no final da primeira")

# ----------------------------------------------------------------------

# 5. Escreva um programa que leia a idade e o primeiro nome de
# várias pessoas. Seu programa deve terminar quando uma
# idade negativa for digitada. Ao terminar, seu programa deve
# escrever o nome e a idade da pessoa mais jovem e mais
# velha
nome_jovem = ""
idade_jovem = 999
nome_velha = ""
idade_velha = 0

while True:
    idade = int(input("Digite a idade: "))
    if idade < 0:
        break
    
    nome = input("Digite o nome: ")
    
    if idade < idade_jovem:
        idade_jovem = idade
        nome_jovem = nome
    
    if idade > idade_velha:
        idade_velha = idade
        nome_velha = nome

print("Pessoa mais jovem:", nome_jovem, "com", idade_jovem, "anos")
print("Pessoa mais velha:", nome_velha, "com", idade_velha, "anos")

# ----------------------------------------------------------------------

# 6. Faça um programa que, dada uma string, diga se ela e um
# palíndromo ou não. Lembrando que um palíndromo e uma
# palavra que tenha a propriedade de poder ser lida tanto da
# direita para a esquerda como da esquerda para a direita
texto = input("Digite uma palavra ou frase: ")
texto = texto.lower().replace(" ", "")

texto_invertido = ""
for letra in texto:
    texto_invertido = letra + texto_invertido

if texto == texto_invertido:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")