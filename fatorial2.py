def fatorial(n):
    fat = 1
    cont = n
    while cont > 1:
        fat *= cont
        cont -= 1
    return fat

m = int(input())
n = int(input())

r= fatorial(m)/((fatorial(m-n))*fatorial(n))
print(r)