import random

attemps = 0
number_list = list(range(1, 31))
number = random.choice(number_list)
running = True

while running:
    guess = float(input("Guess a whole number: "))
    if guess == number:
        attemps = attemps + 1
        running = False
    elif guess > number:
        print(f"The number is less than ", guess)
        attemps = attemps + 1
    elif guess < number:
        print(f"The number is greater than ", guess)
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