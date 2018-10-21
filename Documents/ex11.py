from random import *
correct = 0
guess = 0
rando = randint(0, 101)

print("Time to pick a number!!!")
input("[ENTER]")
while correct == 0:
	guess = input("Guess a number between 0 and 100!")
	if int(guess) == rando:
		correct = 1
		print("Waayyyy congrats you did it! XD")
	if int(guess) < rando:
		print("Guess higher!")
	elif int(guess) > rando:
		print("Guess lower ;)")
	input("[ENTER]")