def factorial(n):
    if n<= 1:
        return 1
    else:
        return n*factorial(n-1)
    

def euler (n):
    if n==0:
        return 1
    return 1/factorial(n) +euler(n-1)

print(euler(0))
print (euler(1))
print(euler(20)) #sin truncar
print(round(euler(20),5)) #con truncar