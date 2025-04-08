'''
Tuplas sao parecido com listas

existem duas diferencas

1-Sao representadas por ()
print(type(()))

2-As tuplas sao imutaveis: Ao se criar uma tupla ela nao muda . Toda operacao em uma Tupla gera uma nova Tupla
____________________________________________________________________________________________________________________
#Cuidado 1: As tuplas sao representadas por () mas :
tupla = (1,2,3,4,5)
print(tupla)

print(type(tupla))
 
tupla2 = 1,2,3,4,5
print(tupla2)
print(type(tupla2))

#cuidado 2: tuplas com 1 elemento

tupla3 = (1) #isso nao 'e uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = 1, #'e uma tupla
print(tupla4)
print(type(tupla4))

#conclusao: Podemos concluir que tuplas sao definidas pela virgula e nao pelo parentese
_________________________________________________________________________________________________________________________

#podemos gerar um tupla com range
tupla = tuple(range(11))
print(tupla)
____________________________________________________________________________________________________________________

#desempacottar tupla
tupla=('Salve salve familia','é isso ae ','deqieeeeeeeeee')

escola, curso,cu = tupla
print(escola)#vai para variavel do indice 0
print(curso)#vai para a variavel do indice 1
print(cu)#vai para a variavel do indice 2
_____________________________________________________________________________________________________________________

#metodos para adicao e remocao de elementos nas tuplas nao existe por conta das tuplas nao poderem mudar
#soma, valor maximo, valor minimo e tamanho valem a mesma coisa
#se os valores forem reais 

tupla=(1,2,3,4,5)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))
_______________________________________________________________________________________________________________

#concatenacao de tuplas:

tupla = (1,2,3,4,5)
tupla2=(2,5,4)
print(tupla+tupla2)#sao imutaveis, nao mudam
print(tupla)
print(tupla2)

_______________________________________________________________________________________________________________
#verificar se ta contido na tupla
tupla = 1,2,3,
print(3 in tupla)
print(33 in tupla)
_______________________________________________________________________________________________________________

#iterando uma tupla

tupla = (1,2,3,)

for i in tupla:
    print(i)

for indice, valor in enumerate(tupla):
    print(indice,valor)
'''

#contando elementos 
tupla = ('a','b','c','d')
print(tupla.count('b'))

escola = tuple('CUUUUUUUUUU')
print(escola)

print(escola.count('U'))
