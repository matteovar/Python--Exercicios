import numpy
escrever = open('resultados.txt', 'w')
tabuleiro = numpy.matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
def jogar(tabuleiro):
    while True:
        count, cond = 0, 0
        print(tabuleiro)
        print("vez do Jogador 1")
        while True:
            move = input("digite a posição que voce quer marcar, sendo linha e coluna, separadas por virgula: ")
            move = move.split(',')
            try:
                move[0], move[1] = int(move[0]), int(move[1])
                if tabuleiro[move[0] - 1,move[1] - 1] != 0:
                    print("não é um movimento válido")
                else:
                    tabuleiro[move[0] - 1, move[1] - 1] = 1
                    print(tabuleiro)
                    count += 1
                    break
            except (ValueError, IndexError):
                print("essa posição nao consta no tabuleiro, digite novamente")
        if count == 9:
            print("empate")
            escrever.write("empate")
            break
        for i in range(3):
            if tabuleiro[i, 0] == 1 and tabuleiro[i, 1] == 1 and tabuleiro[i, 2] == 1:
                print("Jogador 1 venceu")
                escrever.write("jogador 1 venceu")
                cond = 1
                break
            elif tabuleiro[0,i] == 1 and tabuleiro[1,i] == 1 and tabuleiro[2,i] == 1:
                print("Jogador 1 venceu")
                escrever.write("jogador 1 venceu")
                cond = 1
                break
        if tabuleiro[0,0] == 1 and tabuleiro[1,1] == 1 and tabuleiro[2,2] == 1:
            print("Jogador 1 venceu")
            escrever.write("jogador 1 venceu")
            cond = 1
        elif tabuleiro[0,2] == 1 and tabuleiro[1,1] == 1 and tabuleiro[2,0] == 1:
            print("Jogador 1 venceu!")
            escrever.write("jogador 1 venceu")
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
                    print("não é um movimento válido")
                else:
                    tabuleiro[move[0] - 1, move[1] - 1] = 2
                    count += 1
                    break
            except (ValueError, IndexError):
                print("essa posição nao consta no tabuleiro, digite novamente")
        if count == 9:
            print("empate")
            escrever.write("empate")
            break
        for i in range(3):
            if tabuleiro[i, 0] == 2 and tabuleiro[i, 1] == 2 and tabuleiro[i, 2] == 2:
                print("Jogador 2 venceu")
                escrever.write("jogador 2 venceu")
                cond = 1
                break
            elif tabuleiro[0,i] == 2 and tabuleiro[1,i] == 2 and tabuleiro[2,i] == 2:
                print("Jogador 2 venceu")
                escrever.write("jogador 2 venceu")
                cond = 1
                break
        if tabuleiro[0,0] == 2 and tabuleiro[1,1] == 2 and tabuleiro[2,2] == 2:
            print("Jogador 2 venceu")
            escrever.write("jogador 2 venceu")
            cond = 1
        elif tabuleiro[0,2] == 2 and tabuleiro[1,1] == 2 and tabuleiro[2,0] == 2:
            print("Jogador 2 venceu")
            escrever.write("jogador 2 venceu")
            cond = 1
        if cond == 1:
            break
        if count == 9:
            print("empate")
            escrever.write("empate")
            break
def main(tabuleiro):
        flag = True
        while flag == True:
            tabuleiro = numpy.matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
            jogar(tabuleiro)
            reset = input("gostaria de continuar jogando? se sim, digite 1, caso não, digite qualquer coisa:")
            if reset != "1":
                print("Voce saiu....")
                escrever.close()
                flag = False
main(tabuleiro)