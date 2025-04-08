'''

if 18 in lista5:
    print("ele ta")
else:
    print("Nao ta poha")

#ordena a lista
lista.sort()
print(lista)

# conta quantas tem
print(lista.count(8))
print(lista5.count('m'))

#adiciona na lista
lista.append(52)
print(lista)

#nao da certo, da erro
#lista.append(12,52,'matteo')
#print(lista)

#da certo e coloca uma lista dentro de outra lista
lista.append([12,52,'matteo'])
print(lista)

#ver se a lista esta dentro da lista
if [12,52,'matteo'] in lista:
    print("achei otario")
else:
    print('nada')

#coloca os numeros na lista e nao coloca como lista
lista.extend([123,44,59])
print(lista)

#inverte a lista
#forma1
lista.reverse()
print(lista)

amigos.reverse()
print(amigos)

#forma2
print(lista[::-1])
print(amigos[::-1])

#copiar lista
lista6 = amigos.copy()
print(lista6)

#tamanho da lista
print(len(lista))

#remover o ultimo elemento
lista.pop()
print(lista).

#remover pelo indice
lista.pop(5)
print(lista)

#remover todos
lista.clear()
print(lista)

#repetir a lista n vezes
lista = lista*4
print(lista)

#string para lista
curso ='meu pau de assas'
curso = curso.split()
print(curso).

#junta os elementos da lista
lista6 = ['pega','no','meu','pau']
curso = ' '.join(lista6)
print(curso)

#iterando a lista
for i in lista:
    print(i)

#iterando a lista

#ex 1
soma =0 
for i in lista:
    print(i)
    soma += i
print(soma).

#ex2

carrinho=[]
produto =','

while produto!='sair':
    print('Adiciona na lista ou digite "sair" para sair' )
    produto = input()
    if produto !='sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)


#acessar os elementos da lista
#           0         1       2        3
cores= ['vermelho','roxo','branco','amarelo']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

#acessar os elementos mas de forma inversa

print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])

for cor in cores:
    print(cor)

indice =0
while indice <len(cores):
    print(cores[indice])
    indice +=1

#indice das cores
for indice,cor in enumerate(cores):
    print(indice,cor)

#achar o valor de algum indice
print(lista.index(2))
print(lista.index(4))
'''
lista = [1,2,3,5,5,6,8,8,4]
amigos = ['a','b','c','d','e','f','g','h','i','j','k']
lista4 =list(range(0,12))
lista5 = list("meu pau")


cores= ['vermelho','roxo','branco','amarelo']

