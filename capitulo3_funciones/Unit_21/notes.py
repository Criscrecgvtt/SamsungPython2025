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


