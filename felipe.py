vetor = []
a =int(input("Digite o primeiro numero: "))
vetor.append(a)
b =int(input("Digite o primeiro numero: "))
vetor.append(b)
c =int(input("Digite o primeiro numero: "))
vetor.append(c)
print(vetor)

def biggestNumber(vetor):
    if (vetor[0]>vetor[1] and vetor[0]> vetor[2]):
        return vetor[0]
    elif (vetor[1]>vetor[0] and vetor[1]> vetor[2]):
        return vetor[1]
    else:
        return vetor[2]
    return vetor

def main():
    print(biggestNumber(vetor))
main()