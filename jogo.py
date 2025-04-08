import numpy
#escrever = open('resultados.txt', 'w')
tabuleiro = numpy.matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
count,cond = 0,0

while True:
    print(tabuleiro)
    print("vez do Jogador 1")
    while True:
        move = input("digite a posição que voce quer marcar, sendo linha e coluna, separadas por virgula: ")
        move = move.split(',')
        try:
            move[0], move[1] = int(move[0]), int(move[1])
            if tabuleiro[move[0] - 1,move[1] - 1] != 0:
                print("Invalid Move")
            else:
                tabuleiro[move[0] - 1, move[1] - 1] = 1
                print(tabuleiro)
                count += 1
                break
        except (ValueError, IndexError):
            print("Invalid Coordinates, try again ")
    if count == 9:
        print("empate")
        break
    for i in range(3):
        if tabuleiro[i, 0] == 1 and tabuleiro[i, 1] == 1 and tabuleiro[i, 2] == 1:
            print("Jogador 1 venceu")
            cond = 1
            break
        elif tabuleiro[0,i] == 1 and tabuleiro[1,i] == 1 and tabuleiro[2,i] == 1:
            print("Jogador 1 venceu")
            cond = 1
            break
    if tabuleiro[0,0] == 1 and tabuleiro[1,1] == 1 and tabuleiro[2,2] == 1:
        print("Jogador 1 venceu")
        cond = 1
    elif tabuleiro[0,2] == 1 and tabuleiro[1,1] == 1 and tabuleiro[2,0] == 1:
        print("Jogador 1 venceu!")
        cond = 1
    if cond == 1:
        break
    print("vez do Jogador 2")
    while True:
        move = input("digite a posição que voce quer marcar, sendo linha e coluna, separadas por virgula: ")
        move = move.split(',')
        try:
            move[0], move[1] = int(move[0]), int(move[1])
            if tabuleiro[move[0] - 1,move[1] - 1] != 0:
                print("Invalid Move")
            else:
                tabuleiro[move[0] - 1, move[1] - 1] = 2
                count += 1
                break
        except (ValueError, IndexError):
            print("Invalid Coordinates, try again ")
    if count == 9:
        print("empate")
        break
    for i in range(3):
        if tabuleiro[i, 0] == 2 and tabuleiro[i, 1] == 2 and tabuleiro[i, 2] == 2:
            print("Jogador 2 venceu")
            cond = 1
            break
        elif tabuleiro[0,i] == 2 and tabuleiro[1,i] == 2 and tabuleiro[2,i] == 2:
            print("Jogador 2 venceu")
            cond = 1
            break
    if tabuleiro[0,0] == 2 and tabuleiro[1,1] == 2 and tabuleiro[2,2] == 2:
        print("Jogador 2 venceu")
        cond = 1
    elif tabuleiro[0,2] == 2 and tabuleiro[1,1] == 2 and tabuleiro[2,0] == 2:
        print("Jogador 2 venceu")
        cond = 1
    if cond == 1:
        break
    if count == 9:
            print("empate")
            break
    #escrever.write("jogador x venceu")

print("Thank you for playing!")