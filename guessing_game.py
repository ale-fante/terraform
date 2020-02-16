import random

random_num = random.Random()

number = random_num.randrange(1, 1000)

guesses = 0
message = ""

while True:
	guess = int(input(message + "\nGuess my number between 1 and 1000: "))

	guesses += 1

	if guess > numbere:
		messagee += str(guess) + " is too high.\n"
	elif guess < number:
		mssage += str(guess) + " is too low.\n"
	else:
		break

input("\n\nGreat, you got it in " + str(guesses)+ " gusses!\n\n")
