def fibonacci (n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2)) 
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))


    