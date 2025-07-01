f = open("hola.txt", 'w')
for i in range(50):
    f.write("8=> \n")
f.close()

l = open("hola.txt", 'r')
while True:
    line = l.readline()
    if not line:  # Si la línea está vacía, fin del archivo
        break
    print(line, end='')  # 'end' evita saltos de línea extra

l.close()
