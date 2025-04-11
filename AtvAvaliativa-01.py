import random


jogando = True
while jogando == True:
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

        if count == 6:
            print("\n dica")

        pc=0
        pc1=False
        pc2=False
        pc3=False
        pc4=False

        palpite = int(input("\nDigite seu palpite: "))
        print("")

        p1 = palpite/1000
        p1 = int(p1)

        if p1 == n1:     #se estiver na posiçao correta, pc+1
            pc+=1
            pc1=True  

        p2 = (palpite%1000)/100
        p2 = int(p2)
        if p2 == n2:     #se estiver na posiçao correta, pc+1
            pc+=1
            pc2=True

        p3 = (palpite%100)/10
        p3 = int(p3)
        if p3 == n3:     #se estiver na posiçao correta, pc+1
            pc+=1
            pc3=True

        p4 = palpite%10
        if p4 == n4:     #se estiver na posiçao correta, pc+1
            pc+=1
            pc4=True

        count+=1
        print(count,"° tentativa: ")

        print(pc," números na posição CORRETA")
        pe = 4-pc
        print(pe," números na posição ERRADA\n")

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
    jogando = int(input("Jogar mais uma vez? 1=sim / 2=não"))
    if jogando == 0:
        break
    else:
        pass