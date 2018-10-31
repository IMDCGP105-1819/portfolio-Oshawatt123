# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
warnings = 0

def load_words():
	"""
	Returns a list of valid words. Words are strings of lowercase letters.

	Depending on the size of the word list, this function may
	take a while to finish.
	"""
	print("Loading word list from file...")
	# inFile: file
	inFile = open(WORDLIST_FILENAME, 'r')
	# line: string
	line = inFile.readline()
	# wordlist: list of strings
	wordlist = line.split()
	print("  ", len(wordlist), "words loaded.")
	return wordlist



def choose_word(wordlist):
	"""
	wordlist (list): list of words (strings)

	Returns a word from wordlist at random
	"""
	return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
	'''
	secret_word: string, the word the user is guessing; assumes all letters are
	  lowercase
	letters_guessed: list (of letters), which letters have been guessed so far;
	  assumes that all letters are lowercase
	returns: boolean, True if all the letters of secret_word are in letters_guessed;
	  False otherwise
	'''
	# FILL IN YOUR CODE HERE AND DELETE "pass"
	words_correct = 0
	secret_word_list = list(secret_word)
	x = 0
	while x < len(secret_word_list):
		if secret_word_list[x] in letters_guessed:
			words_correct += 1
		x += 1
	
	if words_correct == len(secret_word_list):
		#print("True") - DEBUG
		return True
	else:
		#print("False") - DEBUG
		return False
	
def get_guessed_word(secret_word, letters_guessed):
	'''
	secret_word: string, the word the user is guessing
	letters_guessed: list (of letters), which letters have been guessed so far
	returns: string, comprised of letters, underscores (_), and spaces that represents
	  which letters in secret_word have been guessed so far.
	'''
	# FILL IN YOUR CODE HERE AND DELETE "pass"
	correct_letters = list(secret_word)
	x = 0
	while x < len(correct_letters):
		if correct_letters[x] not in letters_guessed:
			correct_letters.remove(correct_letters[x])
			x -= 1
		x += 1
	#print(correct_letters) - DEBUG
	secret_word_list = list(secret_word)
	stringthing = ""
	x = 0
	while x < len(secret_word_list):
		if secret_word_list[x] in correct_letters:
			stringthing += secret_word_list[x] + " "
		else:
			stringthing += "_ "
		x += 1
	return stringthing

def get_available_letters(letters_guessed):
	'''
	letters_guessed: list (of letters), which letters have been guessed so far
	returns: string (of letters), comprised of letters that represents which letters have not
	  yet been guessed.
	'''
	# FILL IN YOUR CODE HERE AND DELETE "pass"
	#string.ascii_lowercase
	
	alph_list = list(string.ascii_lowercase)
	x = 0
	while x < len(alph_list):
		if alph_list[x] in letters_guessed:
			#print("Hooray") - DEBUG
			alph_list.remove(alph_list[x])
			x -= 1
		x += 1
	return alph_list
	#alph_list can easily be turned into a string and returned but I personally find the printed
	#list much easier to read, so I will leave it like this in my version of hangman

def hangman(secret_word):
	'''
	secret_word: string, the secret word to guess.

	Starts up an interactive game of Hangman.

	* At the start of the game, let the user know how many
	  letters the secret_word contains and how many guesses s/he starts with.

	* The user should start with 6 guesses

	* Before each round, you should display to the user how many guesses
	  s/he has left and the letters that the user has not yet guessed.

	* Ask the user to supply one guess per round. Remember to make
	  sure that the user puts in a letter!

	* The user should receive feedback immediately after each guess
	  about whether their guess appears in the computer's word.

	* After each guess, you should display to the user the
	  partially guessed word so far.

	Follows the other limitations detailed in the problem write-up.
	'''
	
	guesses = 6
	warnings = 0
	word_length = len(secret_word)
	letters_guessed = []
	secret_word_list = list(secret_word)
	vowels = ["a", "e", "i", "o", "u"]
	print(f"The secret word has {word_length} letters!!")
	print("Can you guess them all before you run out of guesses :0 WHO KNOWS!?!?")
	## Loop through as long as they have guesses and don't know the word
	while guesses > 0 and is_word_guessed(secret_word, letters_guessed) == False:
		# Display number of guesses and available letters
		print(f"You have {guesses} guesses left")
		print("Available letters: " + str(get_available_letters(letters_guessed)))
		# Get guessed letter and update list
		guess = input("Please guess a letter: ")
		guess = guess.lower()
		if guess.isalpha():
			if guess in letters_guessed:
				print("You have already guessed that. You have been given a warning")
				warn()
			else:
				#################################### NORMAL GAME #####################################
				letters_guessed.append(guess)
				# Some dialog for the player
				if guess in secret_word_list:
					print("Congrats! That's in the word!")
				else:
					print("Better luck next time!")
					if(guess in vowels):
						guesses -= 2
					else:
						guesses -= 1
				#full word is guessed?
				if(is_word_guessed(secret_word, letters_guessed)):
					print("WOW! You're the most successful contestant we've ever had!!!")
					print("gg wp")
					return
				print("The word so far: " + str(get_guessed_word(secret_word, letters_guessed)))
		else:
			################################## INVALID SYNTAX ###################################
			print("Not valid input. Please use only letters")
			warn()
		print("#############################################")
		print("############# THE NEXT ROUND ################")
		print("#############################################")

def warn():
	warnings += 1
	if warnings%3 == 0:
		guesses -= 1
		print("You have lost a guess due to occurring 3 warnings")
	print(f"WARNINGS: {warnings}")
	print(f"Guesses left: {guesses}")

def Start():
	secret_word = choose_word(wordlist)
	#Extra cut-scene stuff to ward off tiredness
	cutscene = input("Do you wish to participate in the entry 'cut-scene'? (Y/N) : ")
	if cutscene == "N" or cutscene == "n":
		print("Okay then")
	else:
		print("Welcome to hangman! Today you face-off against our most formidable opponent!")
		input("[ENTER]")
		print("THE MIGHTY COMPUTER")
		print("*the crowd goes wiiild aaahhhhh* 'OMG I LOVE YOUUUU' *more screaming and wooting*")
		input("[ENTER]")
		print("And our newest challenger!!!!!")
		print("Wait... what was their name again?")
		name = input("What is your name? : ")
		print(f"Oh, yes! I remembered that! {name}!")
		print("*one guy throws his plastic beer bottle at you from the stands*")
		input("[ENTER]")
		print("*crickets*")
		input("[ENTER]")
		print("Okay then... that was.. well.... the least dramatic entrance we've ever had!")
		print("Onto the game!!!")
	hangman(secret_word)
	print(secret_word)
	
	############## "Start()" Things Down Here #############
Start()