import random

secret_number = random.randint(1, 100)

print("Welcome to Number Guessing Game!")
print("I have selected a number between 1 and 100.")

guess = 0
attempts = 0
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess > secret_number:
        print("Too high!")

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Total attempts:", attempts)
        print("Congratulations! You guessed correctly!")