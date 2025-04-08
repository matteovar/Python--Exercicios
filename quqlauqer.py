lado1=int(input("lado1:"))
lado2=int(input("lado2:"))
lado3=int(input("lado3:"))
if lado1==lado2 and lado1==lado3 and lado2==lado3:
    print("equilatero")
elif lado1==lado2 and lado1!=lado3 or lado1==lado3 and lado2!=lado1 or lado3==lado2 and lado1!=lado2:
    print("isoceles")
c