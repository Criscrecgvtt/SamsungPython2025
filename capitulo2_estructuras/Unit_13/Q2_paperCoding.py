matriz = []
n = 4
 
for i in range(n):
    linea=[]
    for j in range (n):
        linea.append(i*n+j+1)
    matriz.append(linea)

for fila in matriz:
    for elemento in fila :
        print(elemento,sep=" ",end=" ")
    print()