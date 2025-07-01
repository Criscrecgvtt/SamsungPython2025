import random as rd
matriz = []
n = 4

for i in range(n):
    fila =[]
    for j in range (n):
        fila.append(rd.randint(1,100))
    matriz.append(fila)
print(matriz)