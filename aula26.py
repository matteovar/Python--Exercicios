nome = str(input("digita ae: "))
print(nome)

lista = [10, 50, 1, 25, 5, ]
print(lista)

nome = "Matteo"
lista = [2, 4, 6, 8]
for letra in nome:
    print(letra)

for numero in lista:
    print(numero)

for numero in range(0, 10):
    print(numero)

for valor in enumerate(nome):
    print(valor)

qtd = int(input("Quantas vezes esse loop deve rodar"))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'informe o{n}/{qtd} valor'))
    soma += num
print(f'Imprimindo', soma)


nome2 = input("Digita ae: ")
for num3 in range(1, 8):
    print(f'{nome2*num3}')

nome = 'felipe gay'
for num in range(1, 11):
    print(f'{nome * num}')
