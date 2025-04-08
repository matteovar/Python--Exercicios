times_ganhadores = []
meu_arquivo = open('resultado_jogos.txt', 'r',encoding='utf8')


for linha in meu_arquivo:
    registro_time = linha.rstrip()
    info_time = registro_time.split(':')
    nome_time_1 = info_time[0]
    gols_time_1 = int(info_time[1])
    nome_time_2 = info_time[2]
    gols_time_2 = int(info_time[3])

    if gols_time_1 > gols_time_2:
        times_ganhadores.append(nome_time_1)
    elif gols_time_1 == gols_time_2:
        pass
    else:
        times_ganhadores.append(nome_time_2)

    gols1, gols2, gols3, gols4 = 0, 0, 0, 0
    for i in times_ganhadores:
        if 'Corinthians' in i:
            gols1 += 1
        elif 'Guarani' in i:
            gols2 += 1
        elif 'Palmeiras' in i:
            gols3 += 1
        else:
            gols4 += 1 
    
    print(f'CORINTHIANS: {gols1} VITÓRIAS')
    print(f'GUARANI: {gols2} VITÓRIAS')
    print(f'PALMEIRAS: {gols3} VITÓRIAS')
    print(f'SÃO PAULO: {gols4} VITÓRIAS')

meu_arquivo.close()
