#Receive a radius value from the user and print the circumference and area of a circle
radius = int(input("Give me the radius of the circle: "))
pi = 3.141592

circumference = 2*radius*pi
area = pi*(radius**2)
print("Circumference of a circle =",circumference)
print("Area of a circle =",area)
