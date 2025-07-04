import random

while True:
    levels = {
        "easy": [1, 10, 5],
        "medium": [1, 50, 15],
        "hard": [1, 150, 20],
    }
    mode = "medium"
    number_range = levels[mode] #get an array of the range based on the mode passed
    # gets the last element of the specified array (based on the mode passed); for the allowed number of chances
    guess_chances = number_range[-1]
    number_range.pop() # remaining two elements are passed as the range

    number = random.randint(number_range[0], number_range[1])
    range_prompt = f"{number_range[0]} - {number_range[1]}"

    def start_game():
        guesses = 0
        user_guess = ""
        print(f"\nGuess the number\nYou have {guess_chances} guesses!\nNB: Press 0 to go to main menu")
        print(f"Mode: {mode.capitalize()}\nRange: {range_prompt}")

        while user_guess != number:
            user_guess = int(input("> "))
            guesses += 1
            print(f"you've guessed {guesses} times\n--------------------------")
            if guesses == guess_chances:
                print(f"Guess chances are up!\nThe number was {number}\nTry again\n==============================================")
                start_game()
            elif user_guess == 0:
                print("Main Menu")
                break
            elif user_guess > number_range[1]:
                    print(f"Do not go above your range ({range_prompt})")
            elif user_guess < number_range[0]:
                print(f"Do not go below your range ({range_prompt})")
            elif user_guess < number:
                print("Warmer")
            elif user_guess > number:
                print("Colder")
            elif user_guess == number:
                print(f"You guessed right! The number is {number}")
                start_game()
            else:
                print("Unaccepted value! Restart")


    try:
        menu_selection = int(input('''
Guess the number game
1. Play
2. Choose difficulty
3. How to play
4. Exit
> '''))


        if menu_selection == 1:
            start_game()

        elif menu_selection == 2:
            mode = int(input('''
You have three difficulty levels.
1. Easy (1 to 10)
2. Medium (1 to 50)
3. Hard (1 to 150)
> '''))
            # change modes based on user input
            if mode == 1:
                mode = "easy"
            elif mode == 2:
                mode = "medium"
            elif mode == 3:
                mode = "hard"
            else:
                print("Wrong input. Choose an option between 1 and 3!")

            number_range = levels[mode]
            number = random.randint(number_range[0], number_range[1])
            range_prompt = f"{number_range[0]} - {number_range[1]}"
            start_game()

        elif menu_selection == 3:
            print('''
How To Play Number Guessing Game
---------------------------------
The Objective is simple, guess the number auto-generated by the program.
You have a limited number of guesses so guess right before the chances are used up.
You get a hint of "Warmer" ot "Colder" guiding you near the value.
E.g.:
If the number is 10, any guess below 10 hints "Warmer" and any number
above 10 hints "Colder"
---------------------------------
Use Option 2 on the main menu to choose a difficulty level.
The default mode is Medium (1 to 50). You can choose 1 one out of 3 modes
1. Easy (1 to 10)
2. Medium (1 to 50)
3. Hard (1 to 150)
---------------------------------
Getting the guess right starts another game instance.
To go back to the Main Menu at any point in the game, Press 0
''')
        elif menu_selection == 4:
            exit()

        else:
            print("Invalid Selection")

    except ValueError:
        print("Invalid Selection")