import random
f = open("numeros_aleatorios.txt", 'w')
for i in range(50):
    f.write(str(random.randint(1,100))+"\n")
f.close()

l = open("numeros_aleatorios.txt", 'r')
sum =0
while True:
    line = l.readline()
   
    if not line:  # Si la línea está vacía, fin del archivo
        break
    sum+= int(line.strip())
    
print(sum)
l.close()
