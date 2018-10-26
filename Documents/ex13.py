def remove_dups (L1, L2):
	x = 0
	while x < len(L1):
		if L1[x] in L2:
			print("Hooray")
			L1.remove(L1[x])
			x -= 1
		x += 1
		print(x)
		
L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2)
print(L1)