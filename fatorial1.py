l=[1,2,3, 4,5]
def fatorial(l):
    fat = 0
    for i in range(len(l)):
        fat += l[i]
    return fat

def rfac(n):
    if n==1:
        return 1
    else:
        return n * rfac(n-1)
    
def main():
    print(fatorial(l))

main()