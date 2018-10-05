import random
#generate random number
randnum = random.randint(1,100)
print(randnum)
def number_guess_game():
	usr_in = input("Enter your guess for the number: ")

	diff = randnum - usr_in
        if diff < (-20):
		print("The guess is too high!")
		number_guess_game()
	elif -10 < diff < (0):
		print("The guess is a bit high!")
		number_guess_game()
	elif 0 < diff < 5 :
		print("You're almost there")
		number_guess_game()
	elif 5 < diff < 10 :
		print("Getting closer!Come on!")
		number_guess_game()
	elif 20 < diff < 10:
		print("You are pretty close!")
		number_guess_game()
	elif diff > 20:
		print("The guess is too low!")
		number_guess_game()
	elif usr_in == randnum:
		print("You got the number! Good Job!")
	
	
number_guess_game()