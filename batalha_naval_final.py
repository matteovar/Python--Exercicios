'''
Entrega do Trabalho _- Algoritmos e Programação II
Nós,

Augusto Carrera - 32114842
Matteo Domiciano Varnier - 32158238

declaramos que
todas as respostas são fruto de nosso próprio trabalho,
não copiamos respostas de colegas externos à equipe,
não disponibilizamos nossas respostas para colegas externos ao grupo e
não realizamos quaisquer outras atividades desonestas para nos beneficiar
ou prejudicar outros.
'''
import random
grid=[]

def iniciarGrid(grid):
    for i in range(11):
        lista=[]
        for j in range(11):
            if i == 0:
                lista.append(j)
            elif j == 0:
                lista.append(i)
            elif i != 0 and j != 0:
                lista.append(".")
        grid.append(lista)
    return grid

def imprime():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j],end=" ")
        print("\n")

def posicionar_porta_avioes(grid,p1,p2,orient):
    for i in  range(5):
        if orient==2:
            if p1+i>10:
                return False
            lugar=grid[p1+i][p2]
        else:
            if p2+i>=10:
                return False
            lugar=grid[p1][p2+i]
        if lugar != ".":
            return False
        
    for i in range(5):
        if orient == 2:
            grid[p1+i][p2] = "P"
        else:
            grid[p1][p2+i] = "P"
    return True
    

def posicionar_encouraçado(grid,e1,e2,orient):
    for i in  range(4):
        if orient==2:
            if e1+i>10:
                return False
            lugar=grid[e1+i][e2]
        else:
            if e2+i>=10:
                return False
            lugar=grid[e1][e2+i]
        if lugar != ".":
            return False
        
    for i in range(4):
        if orient == 2:
            grid[e1+i][e2] = "E"
        else:
            grid[e1][e2+i] = "E"
    return True

def posicionar_cruzador(grid,c1,c2,orient):
    for i in  range(3):
        if orient==2:
            if c1+i>10:
                return False
            lugar=grid[c1+i][c2]
        else:
            if c2+i>=10:
                return False
            lugar=grid[c1][c2+i]
        if lugar != ".":
            return False
        
    for i in range(3):
        if orient == 2:
            grid[c1+i][c2] = "C"
        else:
            grid[c1][c2+i] = "C"
    return True

def posicionar_submarino(grid,s1,s2,orient):
    for i in  range(2):
        if orient==2:
            if s1+i>10:
                return False
            lugar=grid[s1+i][s2]
        else:
            if s2+i>=10:
                return False
            lugar=grid[s1][s2+i]
            
        if lugar != ".":
            return False
        
    for i in range(2):
        if orient == 2:
            grid[s1+i][s2] = "S"
        else:
            grid[s1][s2+i] = "S"
    return True

def atirar(grid,x,y):
    posicao=grid[x][y]
    if posicao == '.':
        print ("Agua!!")
        grid[x][y] = "O"
    elif posicao == 'P':
        print ("acertou!!")
        grid[x][y] = "X"
    elif posicao == 'E':
        print ("acertou!!")
        grid[x][y] = "X"
    elif posicao == 'S':
        print ("acertou!!")
        grid[x][y] = "X"
    elif posicao == 'C':
        print ("acertou!!")
        grid[x][y] = "X"
    return grid

def main():

    iniciarGrid(grid)

    sucesso = False
    while not sucesso:
        orient=random.randint(1,3)
        a=random.randint(0,9)
        b=random.randint(0,9)
        sucesso = posicionar_porta_avioes(grid,a,b,orient)
        
        
    sucesso = False
    while not sucesso:
        orient=random.randint(1,3)
        a=random.randint(0,9)
        b=random.randint(0,9)
        sucesso = posicionar_encouraçado(grid,a,b,orient)
        
        
    sucesso = False
    while not sucesso:
        orient=random.randint(1,3)
        a=random.randint(0,9)
        b=random.randint(0,9)
        sucesso = posicionar_cruzador(grid,a,b,orient)
        
        
    sucesso = False
    while not sucesso:
        orient=random.randint(1,3)
        a=random.randint(0,9)
        b=random.randint(0,9)
        sucesso = posicionar_submarino(grid,a,b,orient)
        
    
    imprime()
    cont = 0
    tiro = True
    while tiro == True:
        x = int(input("linha: "))
        y = int(input("coluna: "))
        if x > 10 or y > 10:
            print("Errado, digite novamente")
            x = int(input("linha: "))
            y = int(input("coluna: "))
            posicao=grid[x][y]
        if posicao == 'X':
            print ("Voce ja atacou esse lugar, jogue novamente")
            x = int(input("linha: "))
            y = int(input("coluna: "))
        elif posicao == 'O':
            print ("Voce ja atacou esse lugar, jogue novamente")
            
    

main()
