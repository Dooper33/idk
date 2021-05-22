import random

number = random.randint(1, 10)

track = 1

guess = int(input("Guess a number between 1 and 10: "))

while guess != number:
    guess = int(input("Incorrect! \n \nTry again - Guess the number: "))
    track = track + 1

print()
print("Correct - You Guessed the number! \n It took you", track, "trys before you got the correct number!")

print()
input("Type anything to exit: ")