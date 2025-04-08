def somalista(lista):
    if len(lista)==1:
        return lista[0]
    else:
        return lista[0]+ somalista(lista[1:])

lista=[2,4,6,8,10,12]

print(somalista(lista))