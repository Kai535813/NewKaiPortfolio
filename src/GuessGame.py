import random
playAgain = "yes"
while playAgain == "yes":
    numbers = random.randint(0,100)
    print("Welcome, try to guess the correct number between 0 and 100!")
    while True:
        try:
            Guess = int(input("Input your guess here!: "))
            break
        except ValueError:
            print("Enter a valid integer within the given range")

    Guesses = 1
    while Guess != numbers:
        if Guess > numbers:
            print("Your guess of",Guess,"is too HIGH.")
        elif Guess < numbers:
            print("Your guess of",Guess,"is too LOW.")
        while True:
            try:
                Guess = int(input("Try again: "))
                break
            except ValueError:
                print("Enter a valid integer within the given range")

        Guesses += 1
    print("You guessed correctly on valid attempt",Guesses,"!")
    playAgain = input("Do you want to play again? If so type 'yes': ")
print("Bye bye")


