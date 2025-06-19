#Usage of the random module
import random

number = random.randint(1,100)
print (number)

number_2 = random.randrange(2)
print(number_2)

#Coin tossing problem
print("Start coin tossing game. ")
coin = random.randrange(2)
if coin == 0:
    print("Heads")
else:
    print("Tails")
print("Game finished.")