scores = [100, 90, 95, 90, 80, 70, 0, 80, 90, 90, 0, 90, 100, 75, 20, 30, 50, 90]

n_alumnos = len(scores)//3
print("The total number of students is",n_alumnos)

result = [n for n in range ((len(scores)//3)) if all(scores[n*3+o]!=0 for o in range(3))] #te da los indices

result2 = [scores[i*3:(i+1)*3] for i in range(len(scores) // 3) if all(scores[i*3:(i+1)*3])]

grups_de_3 = map(lambda i: scores[i:i+3], range(0,int(len(scores)),3))
result3 = list(filter(lambda grup: all(grup), grups_de_3)) #all funcinas si en si no hay ningun elemento vacio
# Després filtrem aquells que NO tenen cap 0

#scores[i*3:(i+1)*3], lo que hace esq te va haciendo el slicing de 3 en 3, 
#y luego si todos los scores del la parte que estas slicenado con la i , vas moveindote con el o qiue hace cada 3, y
# todos son diferentes de o , que se ve con el all, entonces hace el filtrado y lo mete
print("The total number os students with a valid score is",len(result2))
print(result)
print(result2)
print(result3)