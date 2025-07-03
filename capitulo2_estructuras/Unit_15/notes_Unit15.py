from collections import defaultdict
import copy

lista_original = [[1, 2], [3, 4]]
copia_shallow = copy.copy(lista_original)

copia_shallow[0][0] = 999

print(lista_original)  # [[999, 2], [3, 4]]

#1.Converting List and tupple into dictionary
    
#1.1 From Lists
keys = ['a','b','c','d']
x = dict.fromkeys(keys)
print(x)

#1.1 From tuples
keys = ('a','b','c','d')
x = dict.fromkeys(keys)
print(x)

#1.2 You can add a default value to the dict like this
y = dict.fromkeys(keys,100)
print(y)

#generadores, si lo usasa luego se quedara en en el ultimo como un puntero
g = (x for x in range(10))
print(g)

#1.4 How to use defaultdic, it creates a default dict with vaues of 0
z = y
z = defaultdict(int)
print(z['z'])  #There is no key z in the dictionary but 
#so you can use default dic as a counter as it automaticalaly puts o un all the values
counter = defaultdict(int)
print(counter)

#2.Print dictionary using loops statements
"""for Key, value in dictionary.items(): #Structure to follow
    Code to repeat"""
    
x = {'a':10,'b':20,'c':30,'d':40}
for key, value in x.items():
    print(key,value)
    
#3.Dictionary in dictionary
terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600
    }
}

print(terrestrial_planet['Venus']['mean_radius'])

#4.Assignment and cpying of double dictionaries
 #Es una copia por referencia por loq x e y apuntan al mismo diccionario
x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x
print(x is y) #igualdad en direccion
#Si queremos hacer una copia por valor
y = x.copy()
print(x is y)#Es falso pq no son el mismo
print(x == y )#Es verdadero pq son iguales, pero no seon el mismo, pero si cambiamos un elemnto , ya seria false

"""
    Por python es todo por referncia con matices, y todos son objetos en python , depende de si son mutables o inmutables
    Objetos mutables : list, dic, set, bytearray
    Objetos inmutables : int, float, str, tuple, bool, frozenset
    Porque modificar un objeto mutable afecta a todas las referencias que apuntan a él.
    Con objetos inmutables, cada cambio crea un nuevo objeto, así que otras variables no se ven afectadas.
    Podemos verle con el id
"""
""" 
    s1 = 'hola'
    s2 = 'hola'

    print(id(s1))
    print(id(s2))
    print(s1 is s2) #TRUE
    
    Python tiene una optimización llamada string interning.
    Cuando asignas el mismo literal de cadena (como 'hola') a dos variables, Python reutiliza el mismo objeto en memoria (por eficiencia
    
    s1 = 'hola'
    s2 = ''.join(['ho', 'la'])  # creada dinámicamente

    print(id(s1))
    print(id(s2))
    print(s1 is s2)  # Ahora da False


"""
#El cambio en la copia afecta a la original, porque las listas internas son compartidas.
lista_original = [[1, 2], [3, 4]]
copia_shallow = copy.copy(lista_original)

copia_shallow[0][0] = 999

print(lista_original)  # [[999, 2], [3, 4]]

#Aquí el cambio no afecta a la original, porque se copió todo, incluso lo que está dentro

lista_original = [[1, 2], [3, 4]]
copia_profunda = copy.deepcopy(lista_original)

copia_profunda[0][0] = 999

print(lista_original)  # [[1, 2], [3, 4]]

#Se ha modificado el diccionario original, porque copy.copy() solo copia la capa exterior, pero las listas y subdiccionarios siguen siendo las mismas referencias.
original = {
    'a': [1, 2, 3],
    'b': {'x': 10}
}

shallow = copy.copy(original)

shallow['a'][0] = 999
shallow['b']['x'] = 777

print(original)#{'a': [999, 2, 3], 'b': {'x': 777}}

# El original no cambia porque deepcopy() copia todo, recursivamente.
original = {
    'a': [1, 2, 3],
    'b': {'x': 10}
}

deep = copy.deepcopy(original)

deep['a'][0] = 999
deep['b']['x'] = 777

print(original) #{'a': [1, 2, 3], 'b': {'x': 10}}