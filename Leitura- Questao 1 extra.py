meu_arquivo = open('itens_pedido.txt','r', encoding="utf8")

for total in meu_arquivo:
    registro_comida = total.rstrip()
    info_produto = registro_comida.split(':')
    quantidade = int(info_produto[0])
    preco = int(info_produto[1])
    produto = info_produto[2]

    print(f'Produto: {produto} - Subtotal: R$ {preco*quantidade}')


    
meu_arquivo.close()
