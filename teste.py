with open('resultado_jogos.txt', 'r', encoding='utf8') as resultados:
    vitorias = []

    for linha in resultados:
        registro_resultado = linha.rstrip()
        info_resultado = registro_resultado.split(':')
        nome_time_1 = info_resultado[0]
        gols_time_1 = int(info_resultado[1])
        nome_time_2 = info_resultado[2]
        gols_time_2 = int(info_resultado[3])

        if gols_time_1 > gols_time_2:
            vitorias.append(nome_time_1)
        elif gols_time_1 == gols_time_2:
            pass
        else:
            vitorias.append(nome_time_2)

    gols1, gols2, gols3, gols4 = 0, 0, 0, 0
    for i in vitorias:
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
