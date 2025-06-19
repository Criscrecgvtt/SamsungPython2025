letter = input("Enter an alphabet letter : ")
vowels = ["a","e","i","o","u"]
if letter.lower() in vowels:
    print(letter,"is a vowel")
else:
    print(letter,"is a consonant")