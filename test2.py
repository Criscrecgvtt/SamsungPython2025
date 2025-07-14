cjt = {6, 3, 7, 12}

# RESOLVER AQUÍ EL EJERCICIO 3

entrada = input("Introduce nº enteros separados por coma: ")
numeros = entrada.split(",")

for i in range(len(numeros)):
    numeros[i] = int(numeros[i])

if len(numeros) != len(set(numeros)):
    print("Hay numeros repetidos")
else:
    numeros_set = set(numeros)
    if numeros_set == cjt:
        print("Estan todos")
    elif cjt.issubset(numeros_set) and len(numeros_set) > len(cjt):
        print("Sobran")
    elif numeros_set.issubset(cjt) and len(numeros_set) < len(cjt):
        print("Faltan")
    else:
        print("Faltan y sobran")
