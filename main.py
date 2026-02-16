import random
import sys

high_score = 1000000

running = True

while running:
    attemps = 0
    number_list = list(range(1, 31))
    number = random.choice(number_list)
    guessing = True
    while guessing:
        guess = int(input("Guess a whole number between 1 and 30: "))
        if guess == number:
            attemps = attemps + 1
            print("You guessed the number!")
            if attemps > 1:
                print(f"It took you ", attemps, " trys.")
            elif attemps == 1:
                print("It took you 1 try!")
            print("""
            Here is a scoring chart! See how you scored:
            1 guess: Artificially intelligent
            2-5 guesses: Amazing
            6-10 guesses: Great
            11-15 guesses: Okay
            16-23 guesses: Bad
            24+ guesses: Awful
                """)
            
            if attemps < high_score:
                high_score = attemps
    
            print(f"Your high score is ", high_score)
            replay = input("Would you like to play again? Type 'yes'/'no': ")
            if replay == "yes":
                break
            elif replay == "no":
                print("Exiting...")
                sys.exit(0)

        elif guess > number:
            print(f"The number is less than ", guess)
            attemps = attemps + 1
        elif guess < number:
            print(f"The number is greater than ", guess)
            attemps = attemps + 1