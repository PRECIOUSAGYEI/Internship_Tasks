import random

def number_guessing_game():
    print("******READY TO KILL ittttttt******")
    print("******WELCOME TO THE GUESSING GAME******")
    print("******YOU ARE A GOOD GUESSER NO MATTER WHAT******")
    print("******DONT STOP TRYING******")
    print("LETS BEGINNNNNNNNN")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")

    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != number_to_guess:
        guess = input("Enter your guess: ")
        try:
            guess = int(guess)
            attempts += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print("Congratulations! You found the number in", attempts, "attempts.")
        except ValueError:
            print("Invalid input. Please enter a number.")

number_guessing_game()

