import random
print("Number Guessing Game")
number=random.randint(1,5)
chances = 0
print("Guess a number between 1 and 9")

while chances<5:
    guess = int(input("Enter your guess :  "))

    if guess == number:
        print("Congratulations You won!!!")
        break

    elif guess<number:
        print("Your guess was too low,Guess a higher number than",guess)

    else:
        print("Your guess was too high,Guess a number lower than",guess)

        chances+=1

if not chances<5:
    print("Your lose!! The number is",number)