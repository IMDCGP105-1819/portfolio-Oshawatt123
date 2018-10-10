hooman_name = input("What is your name?")
hooman_age = int(input("What is your age?")) 					# int() casts the input to be an integer
hooman_height = int(input("What is your height in cm?")) 		# which stops it from being invalid
hooman_weight = int(input("What is your weight in kilograms?")) # later on during calculations
hooman_eye_color = input("What colour are your eyes?")
hooman_hair_colour = input("What colour is your hair?!")

# the following is a bunch of mumble in if statements
print(f"Hello, {hooman_name}, and welcome to the trials of Osiris!")
input("[ENTER")
if hooman_age < 15:
	print("I'm sorry, but you are too young to participate	in these activities. Please return when you have reached age of passing.")
	print("But fine, I will give you a free analysis. Consider yourself lucky, child.")
else:
	print("Are you ready? Let's make our analysis")
input("[ENTER]")
if hooman_height > 160:
	print("Wow. Your height indicates you are a real man. You might just survive....")
else:
	print("Ha! You are a small man. Or rather, small boy! Hahahaha!")
input("[ENTER]")
if hooman_weight > 80:
	print("Crikey. You are packing on the pounds. Should hope it is all muscle or you don't stand a chance.")
else:
	print("You are a light one. Being deft might get you through this.")
input("[ENTER]")
print (f"I hate {hooman_eye_color} eyes.")
print (f"I hate {hooman_hair_colour} hair.")