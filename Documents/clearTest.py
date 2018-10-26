from os import system, name

from time import sleep

def clear():
	if name == 'nt':
		_ = system('cls')


print("Melon /n" * 10)
input("")
clear()