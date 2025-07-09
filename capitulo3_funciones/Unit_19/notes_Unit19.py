#Una funcion lamda es una funcion que se define en el sitio que se usa

print("Suma de 100 y 200: ",(lambda x,y :x+y)(100,200))

#Filter function 

# return True for values over 19, and False for those that are not.
def adult_func(n):
    if n >= 19:
        return True
    else:
        return False

ages = [34, 39, 20, 18, 13, 54]
print('adults_list :')
for a in filter(adult_func, ages):  # filter ages by using filter() function
    print(a, end=' ')

ages = [34, 39, 20, 18, 13, 54]
print('adults list :')
for a in filter(lambda x: x >= 19, ages):  # filter ages using filter() function
    print(a, end=' ')



# MAP Function
a = [1, 2, 3, 4, 5, 6, 7]
square_a = list(map(lambda x: x**2, a))
print(square_a)

# REDUCE function

from functools import reduce

a = [1, 2, 3, 4]
n = reduce(lambda x, y: x + y, a)
print(n)

