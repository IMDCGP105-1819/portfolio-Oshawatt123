fizz = 0
buzz = 0

for x in range(100):
	fizz = 0 #reset fizzbuzz variables
	buzz = 0
	if(x+1)%3 == 0:
		fizz = 1	#setting fizzbuzz based on modulo of 3 or 5
	if(x+1)%5 == 0:
		buzz = 1
	
	if(fizz and buzz):
		print("FizzBuzz!") #printing based off of fuzzbuzz variables
	elif(fizz):
		print("Fizz")
	elif(buzz):
		print("Buzz")
	else:
		print(x+1)