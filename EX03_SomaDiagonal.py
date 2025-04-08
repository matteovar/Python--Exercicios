m=[]
letra = input()

for i in range(2):
    m.append([])
    for j in range(2):
        x = float(input())
        m[i].append(x)
c = 0
s = 0
cont = 0
for i in range(1,0,-1):
    c +=1
    for j in range(c,1):
        s += m[i][j]
        cont += 1

if letra == 'S':
    print('{}'.format(s))

if letra == 'M':
    med = s / cont
    print('{:.1f}'.format(med))
