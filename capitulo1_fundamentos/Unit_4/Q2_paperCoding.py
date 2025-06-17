import math
#Calcular la hipotenusa, con el teorema de pitágoras

height=int(input("Dame la altura del triangulo: "))
base=int(input("Dame la base del triangulo: "))

hipotenusa= math.sqrt(height**2 +base**2)
#hipotenusa= (a**2 +b**2)**(1/2)
print("La hipotenusa es", hipotenusa)
