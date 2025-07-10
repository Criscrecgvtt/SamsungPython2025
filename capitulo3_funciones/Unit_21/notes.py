class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        # Initializes the values by being called when Cat instances are generated.

    # A string expression format of the Cat class
    def __str__(self):
        return 'Cat(name=' + self.name + ', color=' + self.color + ')'
        # A special method that defines string expression format of the Cat class

nabi = Cat('nabi', 'black')   # generate instance nabi
nero = Cat('nero', 'white')   # generate instance nero

print(nabi)
print(nero)


class Cat:
    # Called as a constructor or the initialize method
    def __init__(self, name, color):
        self.name = name        # Generates an instance variable named name
        self.color = color      # Generates an instance variable named color

    # The method that prints the information of a cat
    def meow(self):
        print('My name is {}, color is {}, meow meow~~'.format(self.name, self.color))
        # Defines meow of the Cat class via the def keyword

nabi = Cat('nabi', 'black')    # Generates the instance Nabi
nero = Cat('nero', 'white')    # Generates the instance Nero
mimi = Cat('mimi', 'brown')    # Generates the instance Mimi

nabi.meow()
nero.meow()
mimi.meow()
# meow(), a method of the Cat class, can be called by instances of the Cat, Nabi, Nero and Mimi.

class Circle:
    def __init__(self, name, radius, PI):
        self.__name = name      # instance variable
        self.__radius = radius  # instance variable
        self.__PI = PI          # instance variable

    # Compute the area by multiplying radius**2 to current instance’s PI
    def area(self):
        return self.__PI * self.__radius ** 2


c1 = Circle("C1", 4, 3.14)
print("Area of c1:", c1.area())

c2 = Circle("C2", 6, 3.141)
print("Area of c2:", c2.area())

c3 = Circle("C3", 5, 3.1415)
print("Area of c3:", c3.area())




class Circle:
    PI = 3.1415                # class variable
    def __init__(self, name, radius):
        self.__name = name     # instance variable
        self.__radius = radius # instance variable

    # Computes the area by using Circle’s class variable PI
    def area(self):
        return Circle.PI * self.__radius ** 2
        # A method of the class Circle.
        # Instances refer the class variable through Circle.PI in order to use this method.


c1 = Circle("C1", 4)
print("Area of c1:", c1.area())

c2 = Circle("C2", 6)
print("Area of c2:", c2.area())

c3 = Circle("C3", 5)
print("Area of c3:", c3.area())

class Circle:
    PI = 3.14  # Variable de classe

    def __init__(self, name, radius):
        # Variables d'instància amb doble guió baix (name mangling)
        self.__name = name     
        self.__radius = radius

c1 = Circle("C1", 4)

# __dict__ és un diccionari que conté tots els atributs de l'objecte c1
# Les claus reflecteixen els noms reals de les variables d'instància, amb "name mangling":
# Python transforma __name a _Circle__name internament per protegir-lo de sobreescriptura accidental.
print("Attributes of c1:", c1.__dict__)
# Output: {'_Circle__name': 'C1', '_Circle__radius': 4}

# Per accedir al valor de l'atribut ocult __name, hem d'utilitzar la clau real del diccionari: '_Circle__name'
print("Value of c1's name variable:", c1.__dict__['_Circle__name'])  # Output: C1

# Igual per a __radius, que es guarda com '_Circle__radius'
print("Value of c1's radius variable:", c1.__dict__['_Circle__radius'])  # Output: 4

class A:        # parent class A
    #statements
    pass

class B(A):     # child class B with A as the parent
   # statements
   pass