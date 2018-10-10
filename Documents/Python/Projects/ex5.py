bottles = 99
while bottles >=0: # loops till 0, then enters base case on 0
	if bottles == 0: # base case for the loop
		print("No more bottles of bear on the wall. No more bottles of bear")
		print("Go to the store and buy some more. 99 bottles of bear on the wall...")
		break
	print(f"{bottles} bottles of bear on the wall. {bottles} bottles of bear")
	bottles -= 1
	print(f"Knock one down, pass it around. {bottles} bottles of bear on the wall.")
	