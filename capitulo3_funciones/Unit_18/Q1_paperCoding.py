def sum_to_n (n):
    if n == 1:
        return 1
    else:
        return n+ sum_to_n(n-1)

num = int(input("Enter a number: "))
print(sum_to_n(num))