number = input("Enter an integer: ")
length = len(number)

for i in range(length // 2):
    if number[i] != number[-(i + 1)]:
        print(number, "is not a palindrome number")
        break
else:
    print(number, "is a palindrome number")
