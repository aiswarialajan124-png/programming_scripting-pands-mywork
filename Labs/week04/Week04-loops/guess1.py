numberToGuess = 30
guess = int(input("Please guess the number: "))

while guess != numberToGuess:
    print("Wrong")
    guess = int(input("Please guess again: "))

print("Well done! The number was ", numberToGuess)