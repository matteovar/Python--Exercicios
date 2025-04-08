meu_arquivo = open('times.txt', 'r', encoding="utf8")

lista = []
for linha in meu_arquivo:
    ler = lista.append(linha.rstrip())
    lista.sort()
print(lista)

meu_arquivo.close


