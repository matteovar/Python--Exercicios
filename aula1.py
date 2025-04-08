from typing import TYPE_CHECKING


thislist1 = ['apple','banana','cereja','cu']
if 'apple' in thislist1:
    print('its true')

print(thislist1[2:3]) #limita a lista 
print(len(thislist1)) #tamanho da lista
thislist1.insert(0,'feijao') #inseri um item na posicao
print(thislist1) #printa a lista nova
print(type(thislist1)) # printa o tipo de lista
thislist1[0] = 'cu de cachorro' #substitui o item na posicao especifica
print(thislist1) 