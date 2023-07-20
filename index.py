print("Welcome to this little project I made. It's some games I made.")
choice = input("Make a selection.\n1. Rock, Paper, Scissors\n2. Guess the number\n Type the number here: ")
if choice == "1":
    exec(open("rps.py").read())
elif choice == "2":
    exec(open("guess.py").read())