number = input("Enter an integer: ")
i = 1

for n in number:
    if n == number[-i]:
        i += 1
    else:
        print(number, "is not a palindrome number")
        break
else:
    print(number, "is a palindrome number")
