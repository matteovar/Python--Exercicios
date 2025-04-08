import random

def criaMatriz(l,c):
    A = []
    for i in range(l):
        linha = [] # lista vazia
        for j in range(c):        
            linha.append(random.randint(1,10))
        A.append(linha)
    return A

def somaDiagonalPrincipal(M):
    soma=0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i==j:
                soma+=M[i][j]
    return soma

def somaDiagonalSecundaria(M):
    soma=0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i+j==(len(M)-1):
                soma+=M[i][j]
    return soma
            

def imprime(A):
    for i in range(len(A)):            
        print(A[i])

def main():
    l=int(input("Linha: "))
    c=int(input("Coluna: "))
    A = criaMatriz(l,c)
    imprime(A)
    print("Soma Diagonal Secundaria: ", somaDiagonalSecundaria(A))

main()





