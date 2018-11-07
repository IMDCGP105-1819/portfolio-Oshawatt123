def fib(x):
	if x<=1:
		return x
	else:
		return fib(x-1) + fib(x-2)

print(fib(int(input("What Number of the fibonacci do you want? eg (5)th number: "))-1))






