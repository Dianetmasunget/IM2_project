import random

randnum = random.randint(1,100)

guess = None
attempts = 0

while guess != randnum:
    guess = int(input("Enter number: "))
    attempts += 1

    if guess < randnum:
        print("Too Low")
    elif guess > randnum:
        print("Too high!")
    else:
        print("Correct!")
        print(f"Attempts: {attempts}")