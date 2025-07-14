"""
### Ejercicio 1

Dadas tres listas `l1`,`l2`y `l3`, nos piden obtener una lista en la que cada elemento sea la suma de los tres elementos situados en la misma posición en las listas originales, siempre y cuando la paridad entre los tres elementos coincida. Para el siguiente ejemplo:

```
l1 = [1, 2, 3, 4, 5, 6]
l2 = [3, 3, 5, 6]
l3 = [1, 1, 7, 2, 8, 7, 8, 9]
```

el resultado sería `[5, 15, 12]`, que corresponde a las sumas de:

- `5 = 1+3+1` en la posición 0
- `15 = 3+5+7` en la posición 2
- `12 = 4+6+2` en la posición 3

No se suman los valores 2+3+1 de la posición 1 porque 2 es par mientras que 3 y 1 son impares.
"""
l1 = [1, 2, 3, 4, 5, 6]
l2 = [3, 3, 5, 6]
l3 = [1, 1, 7, 2, 8, 7, 8, 9]


# RESOLVER AQUÍ EL EJERCICIO 1

res = []
min_List = min(l1, l2, l3, key=len)
for i in range(len(min_List)):
    if (l1[i]%2==l2[i]%2==l3[i]%2):
        suma = l1[i]+l2[i]+l3[i]
        res.append(suma)
print(res)    

"""
### Ejercicio 2

Nos dan una lista de cadenas:

```python
ls = ["El blanco oso", "El oso blanco", "Un día caluroso", "Blanco el oso", 
      "O blance loso", "No parece algo que tenga que aparecer"]

```

Y nos piden devolver otra lista con todas las cadenas de la lista que tengan el mismo número de caracteres de cada tipo (mismo nº 'a', mismo nº de 'b',... incluidos espacios en blanco, comas etc...) que la primera cadena de la lista.

A la hora de contar el nº caracteres de cada tipo hay que ignorar que sean mayúsculas o minúsculas. Es decir, "Aba" y "Baa" se considera que cumplen la condición porque tienen 2 'a' y 1 'b', pero "Aba" y "aBB" no cumplen la condición.

Para el ejemplo de la lista `ls` el resultado sería:

```python
['El blanco oso', 'El oso blanco', 'Blanco el oso', 'O blance loso']
```

"""
ls = ["El blanco oso", "El oso blanco", "Un día caluroso", "Blanco el oso", "O blance loso", "No parece algo que tenga que aparecer"]

# RESOLVER AQUÍ EL EJERCICIO 2

primera_cadena = (sorted((ls[0]).lower()))
res = []
for i in ls :
    cadena = sorted((i).lower())
    if cadena == primera_cadena:
        res.append(i)

print(res)

""" 
### Ejercicio 3

Dado el siguiente conjunto de números enteros:

```python
cjt = {6, 3, 7, 12}
```

Se pide realizar un programa que pida al usuario una serie de números enteros separados por coma.

Puedes asumir que el usuario no se equivoca al introducir los números.

A continuación, el programa mostrará uno de estos mensajes:

- `Hay números repetidos` se mostrará cuando el usuario haya introducido más de una vez un mismo número.
- `Estan todos`si el usuario ha introducido, sin repetir, los números del cjt.
- `Sobran` si el usuario ha introducido todos los nº del cjt y alguno más.
- `Faltan` si todos los nº que ha escrito el usuario está en el cjt pero falta alguno.
- `Faltan y sobran` en cualquier otro caso.


Ejemplo de ejecución:

```
Introduce nº enteros separados por coma: 3,6,7,7,12
Hay numeros repetidos
```

Otro ejemplo:

```
Introduce nº enteros separados por coma: 3,12,7,6
Estan todos
```

Otro ejemplo:

```
Introduce nº enteros separados por coma: 3,6
Faltan
```

Otro ejemplo:

```
Introduce nº enteros separados por coma: 1,2,3,6,7,12
Sobran
```

Otro ejemplo:

```
Introduce nº enteros separados por coma: 1,2,3,6
Faltan y sobran
```

"""

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