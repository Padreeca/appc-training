# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o 
# valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("Valor inválido!")
    nota = float(input("Digite uma nota entre 0 e 10: "))

print("Nota válida:", nota)

# ----------------------------------------------------------------------

# 2. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

numero = 1

while numero <= 50:
    if numero % 2 != 0:
        print(numero)
    numero = numero + 1

# ----------------------------------------------------------------------

# 3. Faça um programa que leia 5 números e informe a soma e a média dos números.

contador = 0
soma = 0

while contador < 5:
    numero = float(input("Digite um número: "))
    soma = soma + numero
    contador = contador + 1

media = soma / 5

print("Soma dos números:", soma)
print("Média dos números:", media)

# ----------------------------------------------------------------------
# Exemplo
# Elaborar um programa que pede a digitação de uma senha. Repetir o processo 
# enquanto a senha não for digitada corretamente. Após 3 tentativas erradas, 
# o processo de leitura deve ser interrompido e encerrado o processo de leitura. 
# Imprimir mensagem de bloqueio de cartão ou senha correta.

senha_correta = "123456"

for tentativa in range(1, 4):
    senha = input("Digite sua senha: ")
    
    if senha == senha_correta:
        print("Senha correta acesso permitido.")
        break
    else:
        print("Senha incorreta. Tentativa", tentativa, "de 3.")
        
    if tentativa == 3:
        print("Cartão bloqueado! Número máximo de tentativas excedido.")