n = int(input("Digite quantos numeros quer na sequencia: "))    #ask the number
ant = 0                     #where it starts
prox = 1                    # next number on the sequence
for i in range(0,n):        # i starts in 0 and ends in n
    print(ant)              
    prim = ant              #creat a variable to ant 
    ant = prox              
    prox += prim            # add the number before to make the next number