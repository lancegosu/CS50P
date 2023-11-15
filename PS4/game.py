import random

# Prompt the user for a level, n. If the user does not input a positive integer, the program should prompt again.
while True:
    try:
        n = input("Level: ")
        if int(n) <= 0:
            continue
        else:
            break
    except ValueError:
        continue

# Randomly generates an integer between 1 and n, inclusive, using the random module.
number = random.randint(1, int(n))

while True:
    try:
        guess = int(input("Guess: "))
        if guess < number:
            print("Too small!")
            continue
        elif guess > number:
            print("Too large!")
            continue
        elif guess == number:
            print("Just right!")
            break
    except ValueError:
        continue