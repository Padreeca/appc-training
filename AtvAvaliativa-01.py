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
            while True:        #tirar while true
                n_dica = random.randint(1,4)

                if n_dica==1 and not pc1:     #se random ==1
                    if pc1%2==0:
                        pc1="par"
                    else:
                        pc1="ímpar"
                    if pc1<5:
                        pc1="<5"
                    else:
                        pc1=">4"

                if n_dica==2 and not pc2:     #se random ==2
                    if pc2%2==0:
                        pc2="par"
                    else:
                        pc2="ímpar"
                    if pc2<5:
                        pc2="<5"
                    else:
                        pc2=">4"

                if n_dica==3 and not pc3:     #se random ==3
                    if pc3%2==0:
                        pc3="par"
                    else:
                        pc3="ímpar"
                    if pc3<5:
                        pc3="<5"
                    else:
                        pc3=">4"

                if n_dica==3 and not pc4:     #se random ==4
                    if pc4%2==0:
                        pc4="par"
                    else:
                        pc4="ímpar"
                    if pc4<5:
                        pc4="<5"
                    else:
                        pc4=">4"        

        pc=0
        pc1=False
        pc2=False
        pc3=False
        pc4=False

        palpite = int(input("\nDigite seu palpite: "))
        print("")

        p1 = palpite/1000
        p1 = int(p1)

        if p1 == n1 or p1==n2 or p1==n3 or p1==n4:
            pc+=1
            if p1 == n1:
                pc1=True 

        p2 = (palpite%1000)/100
        p2 = int(p2)
        if p2 == n1 or p2==n2 or p2==n3 or p2==n4:
            pc+=1
            if p2 == n2:
                pc2=True

        p3 = (palpite%100)/10
        p3 = int(p3)
        if p3 == n1 or p3==n2 or p3==n3 or p3==n4:
            pc+=1
            if p3 == n3:
                pc3=True

        p4 = palpite%10
        if p4 == n1 or p4==n2 or p4==n3 or p4==n4:
            pc+=1
            if p4 == n4:
                pc4=True
            
            

        count+=1
        print(count,"° tentativa: \n")

        print(pc," números CORRETOS")
        # pe = 4-pc
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