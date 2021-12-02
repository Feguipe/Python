a = float(input("Digite o valor do lado a "))
b = float(input("Digite o valor do lado b "))
c = float(input("Digite o valor do lado c "))

if not((a<b+c) and (b<a+c) and (c<a+b)):
    print("Nao e um triangulo")
elif((a!=c) and (a!=b) and (a!=a)):
    print("Triangulo escaleno ")
elif((a==b) and (b==c) and (a==c) ):
     print("Triangulo Equilatero")
else:
    print("Triangulo Isoceles")
