# El slicing no funciona con rangos, osea si funciona pero  devuelve rangos

r = range(10,100,4)
print(r)
print(r[9])
print(r[9:12])

lista = list(r)
lista2 = list(r[9:12])
print(lista)
print(lista2)

#Todos los elementoa menos los n últimos 

#Elementos de caracteres , ordenadcion

print(ord("C")) #Te devuelve el código de ascii
