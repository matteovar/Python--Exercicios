lista1= ['1','2','3','4','5']
def msg():
    print("  Bem vindo ao Quiz sobre Fake News ")
    print("  Voce respondera algumas perguntas sobre fake news e se acertar a questao ganhara alguns pontos" )


def quest1():
    print("Questao 1: Para evitar noticiais falsas, voce deve:")
    print("1- Nao conferir o endereco URL")
    print("2- pesquisar em mais sites de noticias ")
    print("3- confiar em grupos de whattsapp da familia")
    print("4- nao saber quem escreveu o texto")
    print("5- nao ver a noticia somente pelo titulo")
    alter1 =0
    soma = 0
    for i in lista1:
        alter1 = int(input("Alternativa escolhida: "))
        if alter1 == 1:
            print(" Errada!")
            print("Explicacao:")
            print(" O endereco URL é uma das coisas que devem ser chegadas para ver se o site é confiavel")
            print("Outras questoes:")
            print(" (Alternativa2)- Correta!!!É algo mais certo a se fazer, pois pesquisando em outros sites é possivel ver se é verdade ou nao ")
            print(" (Alternativa3)- Errado!!Grupo da familia tem muitas circulacoes de noticias e uma delas podem ser falsas")
            print(" (Alternatica4) -Errado!!Para saber se o texto é verdade, deve ser pesquisado o nome do autor para ver se o mesmo escreve noticias reais")
            print(" (Alternativa5)- Errado!!As vezes o titulo pode te enganar falando de uma coisa porem a noticia nao tem nada haver com o assunto")
            print("*************************************************************************************")
            break
        
        elif alter1 ==2:
            print(" Correta!!!")
            print("Explicacao:")
            print(" É algo mais certo a se fazer, pois pesquisando em outros sites é possivel ver se é verdade ou nao ")
            print("Outras questoes:")
            print(" (Alternativa1)- O endereco URL é uma das coisas que devem ser chegadas para ver se o site é confiavel")
            print(" (Alternativa3)- Errado!!Grupo da familia tem muitas circulacoes de noticias e uma delas podem ser falsas")
            print(" (Alternatica4) -Errado!!Para saber se o texto é verdade, deve ser pesquisado o nome do autor para ver se o mesmo escreve noticias reais")
            print(" (Alternativa5)- Errado!!As vezes o titulo pode te enganar falando de uma coisa porem a noticia nao tem nada haver com o assunto")
            soma +=50
            print("*************************************************************************************")
            break
            
        elif alter1 ==3:
            print(" Errado!!")
            print("Explicacao:")
            print(" Grupo da familia tem muitas circulacoes de noticias e uma delas podem ser falsas")
            print("Outras questoes:")
            print(" (Alternativa1)- O endereco URL é uma das coisas que devem ser chegadas para ver se o site é confiavel")
            print(" (Alternativa2)- Correta!!!É algo mais certo a se fazer, pois pesquisando em outros sites é possivel ver se é verdade ou nao ")
            print(" (Alternatica4) -Errado!!Para saber se o texto é verdade, deve ser pesquisado o nome do autor para ver se o mesmo escreve noticias reais")
            print(" (Alternativa5)- Errado!!As vezes o titulo pode te enganar falando de uma coisa porem a noticia nao tem nada haver com o assunto")
            print("*************************************************************************************")
            break
        
            
            
        elif alter1 ==4:
            print(" Errado!!")
            print("Explicacao:")
            print(" Para saber se o texto é verdade, deve ser pesquisado o nome do autor para ver se o mesmo escreve noticias reais")
            print("Outras questoes:")
            print(" (Alternativa1)- O endereco URL é uma das coisas que devem ser chegadas para ver se o site é confiavel")
            print(" (Alternativa2)- Correta!!!É algo mais certo a se fazer, pois pesquisando em outros sites é possivel ver se é verdade ou nao ")
            print(" (Alternativa3)- Errado!!Grupo da familia tem muitas circulacoes de noticias e uma delas podem ser falsas")
            print(" (Alternativa5)- Errado!!As vezes o titulo pode te enganar falando de uma coisa porem a noticia nao tem nada haver com o assunto")
            print("*************************************************************************************")
            break

            
        elif alter1 ==5:
            print(" Errado!!")
            print("Explicacao:")
            print(" As vezes o titulo pode te enganar falando de uma coisa porem a noticia nao tem nada haver com o assunto")
            print("Outras questoes:")
            print(" (Alternativa1)- O endereco URL é uma das coisas que devem ser chegadas para ver se o site é confiavel")
            print(" (Alternativa2)- Correta!!!É algo mais certo a se fazer, pois pesquisando em outros sites é possivel ver se é verdade ou nao ")
            print(" (Alternativa3)- Errado!!Grupo da familia tem muitas circulacoes de noticias e uma delas podem ser falsas")
            print(" (Alternatica4) -Errado!!Para saber se o texto é verdade, deve ser pesquisado o nome do autor para ver se o mesmo escreve noticias reais")
            print("*************************************************************************************")
            break
            
        else:
            if alter1<=0 or alter1>=6:
                alter1 = input("Valor invalido, digite novamente: ")
            


    

def main():
    msg()
    quest1()
    ponto()

main()