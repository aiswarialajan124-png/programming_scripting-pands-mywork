numberToGuess = 30
guess = int(input("Please guess the number: "))

while guess != numberToGuess:
    if guess < numberToGuess:
        print("Too low")
    else:
        print("Too high")

    guess = int(input("Please guess again: "))

print("Well done! The number was", numberToGuess)