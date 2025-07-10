class Dog:
    def __init__(self,name):
        self.name = name
    
    def bark(self):
        print("{}: woof woof".format(self.name))
        
perrito = Dog("Bingo")
perrito.bark()