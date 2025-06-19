n = int(input("Enter n: "))
suma=1
print()
print("-"*(n*2),"START","-"*(n*2))
print()
for i in range (0,n,1):
    if(i%2 !=0):
        first = suma+n-1
        finish=suma-1
        next=-1
    else:
        first =suma
        finish=suma+n
        next=1
    for j in range(first,finish,next):
        print("{:4d}".format(j),end=" ")
        
    suma+=n  
    print("\n")
    
print("-"*(n*2),"FIN","-"*(n*2))

#Mas eficiente de memoria

"""
n = int(input("Enter n: "))

for i in range(n):
    start = i * n  # el primer número de la fila
    if i % 2 == 0:
        # Fila par → orden ascendente
        for j in range(start + 1, start + n + 1):
            print(j, end=" ")
    else:
        # Fila impar → orden descendente
        for j in range(start + n, start, -1):
            print(j, end=" ")
    print()

"""