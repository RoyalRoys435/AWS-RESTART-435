random = {1,2,3,4,5,6,7,8,9,10}
import random
number = random.randint(1,10)
isGuessRight = False

print("welcome to guess the number!")
print(" The rules are simple. i will think of a number and you will try to guess it")

while isGuessRight != True:
    guess = input("guess a number between 1 and 10 :")
    if int(guess) == number:
        print("you guessed {}. That is correct! you win". format(guess))
        isGuessRight = True
    else:
        print("you guessed {}. sorry that isnt it, try again.". format(guess))
    


