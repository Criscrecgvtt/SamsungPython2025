matriz = []
num = int(input("Dame un número "))

for i in range(num):
    linea = []
    for j in range (num):
        if i%2 == 0:
            if j %2 == 0:
                linea.append(1)
            else:
                linea.append(0)
        else:
            if j %2 == 1:
                linea.append(1)
            else:
                linea.append(0)
    matriz.append(linea)
            
for fila in matriz:
    for elemento in fila:
        print(elemento,end=" ")
    print()