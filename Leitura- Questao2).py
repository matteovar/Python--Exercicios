meu_arquivo = open('times.txt', 'r', encoding="utf8")

lista = []
for linha in meu_arquivo:
    lista.append(linha.rstrip())

jogos=[]
for rodada in range(len(lista)):
    for partida in range(rodada+1, len(lista)):
        jogos.append(lista[rodada] + ' X '+ lista[partida])
        

print(jogos)


meu_arquivo.close
    
    
