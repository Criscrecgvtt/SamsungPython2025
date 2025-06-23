import random

num = random.randint(1,100)
guess= -1
count =0

print("Guess a number between 1 to 100")
while guess != num:
    guess= int(input("Enter a number : "))
    if (guess<num):
        print("Higher!")
    elif guess>num:
        print("Lower!")  
    count+=1
    
print("Congratulations. Total try:",count)