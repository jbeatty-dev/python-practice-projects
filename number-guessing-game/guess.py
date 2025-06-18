import random 

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1, 20.")
print("You have 5 attempts to guess it correctly.")

secret_number = random.randint(1, 20)
attempts = 0
max_attempts = 5

while True: 
    guess = input("Take a guess: ")

    if not guess.isdigit():
        print("Please enter a number.")
        continue
    
    guess = int(guess)
    attempts += 1

    if guess == secret_number:
        print(f"Correct! You guessed it in {attempts} tries.")
        print("Thanks for playing!")
        break

    elif guess < secret_number:
        print("Too low! Try again.")
    else: 
        print("Too high! ")

    # Only check this if the guess was wrong
    if attempts >= max_attempts:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {secret_number}.")
        print("Better luck next time!")
        break
# End of the guessing game code