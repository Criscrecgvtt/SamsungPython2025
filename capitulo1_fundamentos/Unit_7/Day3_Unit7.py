#Instruccion pas , instruccion vacia para que no te de errores 
#Como para dejar un if vacio 
num = int(input("Enter an integer: "))
if num >= 0:
    if num == 0:
        print("It is 0")
    else:
        print("It is positive")
else:
    print("It is negative")