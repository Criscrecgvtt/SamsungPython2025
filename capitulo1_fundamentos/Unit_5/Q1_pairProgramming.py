num = int (input("Enter a 3-digit integer: "))
div = num//100 #El operador // es la division entera
print("Hay un tres en las centenas?",div==3)

#Another way , it needs more checkings
num =  input("Enter a 3-digit integer: ")
print("Hay un tres en las centenas?",num[0]=='3')
