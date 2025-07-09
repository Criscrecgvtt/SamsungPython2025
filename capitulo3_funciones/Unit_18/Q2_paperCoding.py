
def power(x,n):
    if n <1:
        return 1
    else:
        return x*power(x,n-1)
x = int(input("Enter x: "))
n = int (input("Enter n: "))
print(power(x,n))