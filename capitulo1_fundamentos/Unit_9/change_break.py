cadena ="psicologia"
i=0
encontrada= False

while i<len(cadena) and not encontrada:
    if cadena[i] in ["a","e","i","o","u"]:
        encontrada = True
    else:
        print(cadena[i])
    i+=1