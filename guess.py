import os
import random

def clear_console():
    # Clear console screen for different operating systems
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    clear_console()
    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 10)
    guesses_taken = 0

    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        guesses_taken += 1

        if guess == number_to_guess:
            print(f"Congratulations! You guessed the number in {guesses_taken} attempts.")
            break
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thank you for playing!")

play_game()
