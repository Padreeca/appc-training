import random


jogando = 1
while jogando != 0:
    secreto = random.randint(1000,9999)     #biblioteca .random
    print(secreto)

    n1 = secreto/1000  #daria p usar // para pegar só o inteiro
    n1=int(n1)
    print(n1)

    n2 = (secreto%1000)/100
    n2 = int(n2)
    print(n2)

    n3 = (secreto%100)/10
    n3 = int(n3)
    print(n3)

    n4 = (secreto%10)
    print(n4)

    palpite = 0
    count = 0


    while palpite != secreto and count<10:

        if count == 5:
            print("\n dica")
            dica = 0
            while dica == 0:        #tirar while true
                n_dica = random.randint(1,4)
                par_impar_maior_menor = random.randint(1,2)
                if n_dica==1 and not pc1:     #se random ==1
                    if par_impar_maior_menor == 1:
                        if p1%2==0:
                            print("Primeira posição é par")
                            dica = 1
                        else:
                            print("Primeira posição é ímpar")
                            dica = 1
                    else:
                        if pc1<5:
                            print("Primeira posição menor que 5")
                            dica = 1
                        else:
                            print("Primeira posição maior que 4")
                            dica = 1

                if n_dica==2 and not pc2:     #se random ==2
                    if par_impar_maior_menor == 1:
                        if pc2%2==0:
                            print("Segunda posição é par")
                            dica = 1
                        else:
                            print("Segunda posição é ímpar")
                            dica = 1
                    else:
                        if pc2<5:
                            print("Segunda posição menor que 5")
                            dica = 1
                        else:
                            print("Segunda posição maior que 4")
                            dica = 1

                if n_dica==3 and not pc3:     #se random ==3
                    if par_impar_maior_menor == 1:
                        if pc3%2==0:
                            print("Terceira posição é par")
                            dica = 1
                        else:
                            print("Teceira posição é ímpar")
                            dica = 1
                    else:
                        if pc3<5:
                            print("Terceira posição menor que 5")
                            dica = 1
                        else:
                            print("Terceira posição maior que 4")
                            dica = 1

                if n_dica==4 and not pc4:     #se random ==4
                    if par_impar_maior_menor == 1:
                        if pc4%2==0:
                            print("Quarta posição é par")
                            dica = 1
                        else:
                            print("Quarta posição é ímpar")
                            dica = 1
                    else:
                        if pc4<5:
                            print("Quarta posição menor que 5")
                            dica = 1
                        else:
                            print("Quarta posição maior que 4")
                            dica = 1       

        pe=0
        pc1=False
        pc2=False
        pc3=False
        pc4=False

        palpite = int(input("\nDigite seu palpite: "))
        print("")

        p1 = palpite/1000
        p1 = int(p1)

        if p1 == n1:
            pc1 = True    #posição correta do 1
        elif p1 == n2 or p1 == n3 or p1 == n4:
            pe += 1

        p2 = (palpite%1000)/100
        p2 = int(p2)
        if p2 == n2:
            pc2 = True
        elif p2 == n1 or p2 == n3 or p2 == n4:
            pe += 1

        p3 = (palpite%100)/10
        p3 = int(p3)
        if p3 == n3:
            pc3 = True
        elif p3 == n1 or p3 == n2 or p3 == n4:
            pe += 1

        p4 = palpite%10
        if p4 == n4:
            pc4 = True
        elif p4 == n1 or p4 == n2 or p4 == n3:
            pe += 1
            

        count+=1
        print(count,"° tentativa: \n")

        print(pe," números CORRETOS na POSIÇÃO INCORRETA")
        # pe = 4-pe
        # print(pe," números na posição ERRADA\n")

        #printa quais números corretos
        if pc1:
            print(p1,"", end='')
        else:
            print("_ ", end='')
        
        if pc2:
            print(p2,"",end='')
        else:
            print("_ ", end='')

        if pc3:
            print(p3,"", end='')
        else:
            print("_ ", end='')

        if pc4:
            print(p4,"", end='')
        else:
            print("_ ")

        print("-------------------------------")

    print("\n \nCódigo Secreto: ", secreto)

    if palpite!=secreto:
        print("Você perdeu o jogo!")
    else:
        print("Parabens, você acertou na",count,"° tentativa!\n")
    
    print("-------------------------------------------------")
    jogando = int(input("Jogar mais uma vez? 1=sim / 0=não"))
    if jogando == 0:
        break
    else:
        pass