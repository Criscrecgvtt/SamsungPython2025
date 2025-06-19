#Start with fors
for i in range(10):
    print(i,"8=>")
#range is un tipo de datos, propio de pyhton
for i in range(20,10,-2):
    print(i)
#puedes reconvertir range a una lista
print(list(range(0,5,1)))
#tipo de range
print(type(range(3)))
#Puedes hacer cosas chulas
lista= "Hola"
for i in lista:
    print(i)
#Funcion sum
numbers=[10,20,30,40,50]
print("La suma de la lista es",sum(numbers))