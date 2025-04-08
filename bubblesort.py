import random
import time


def vetor(matriz):
    for i in range(100):
        matriz.append(random.randint(1,100))
    return matriz


def BubbleSort(matriz):
    cont=0
    seconds=time.time()
    comparacoes=0
    for i in range(len(matriz)):
        for j in range(len(matriz)-1-i):
            comparacoes+=1
            if matriz[j]>matriz[j+1]:
                temp=matriz[j]
                matriz[j]=matriz[j+1]
                matriz[j+1]=temp
                cont+=1
    tempofinal=time.time()-seconds
    return matriz,cont,comparacoes,tempofinal

def main():
    matriz=[]
    vetor(matriz)
    matriz,cont,comparacoes,tempofinal=BubbleSort(matriz)
    print(matriz)
    print("trocas:",comparacoes)
    print("tempo:",tempofinal)
    print("contador:",cont)
    
main()
    
    
    
main()
                
