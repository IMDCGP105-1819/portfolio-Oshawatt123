lyric = "oh dan oh why do you play TF2 you absolute baboon man man man"

lyric_list = lyric.split(" ") # easy python way to split the song into each word
word_freq = {}

x = 0
# get the frequency of every word in the song
while x < len(lyric_list):
	if lyric_list[x] in word_freq:
		word_freq[lyric_list[x]] += 1
	else:
		word_freq[lyric_list[x]] = 1
	x += 1

	
# bubble sort to sort the list into the right order
# bubble was used as it is easy to code and does the job fine
# the list will never be big enough to run into any major time issues as songs aren't THAT long
def bubsort(list, word_freq):
	length = len(list)
	x = 0
	temp = 0
	sort = 0
	sorted = False
	while x < length and not sorted:
		if word_freq.get(list[x]) > word_freq.get(list[x+1]):
			temp = list[x]
			list[x] = list[x+1]
			list[x+1] = temp
		else:
			sort += 1
		x += 1
		if x == length-1:
			x = 0
		if sort == length:
			sorted = True
	return list
	
def mostcommon(word_freq):
	mostcommonword = []
	mostcommonwordfreq = 0
	for x in word_freq:
		# if the word is the most common, set it as most common word
		if word_freq.get(x) > mostcommonwordfreq:
			mostcommonword = [x]
			mostcommonwordfreq = word_freq.get(x) # completely overwrites whole list to avoid having less common words stuck in there
		# if they have the same frequency then add it to the list (no overwrite)
		elif word_freq.get(x) == mostcommonwordfreq:
			mostcommonword.append(x)
	tpl = (mostcommonword, mostcommonwordfreq)
	return tpl
	
def atleast(word_freq, num):
	wordlist = []
	for x in word_freq:
		# no need to overwrite list like last time as is "at least" so simply added on the end
		if word_freq.get(x) >= num:
			wordlist.append(x)
	# sort the list on frequency for nice presentation
	wordlist = bubsort(wordlist, word_freq)
	#print(wordlist) - DEBUG
	tpl = (wordlist, num)
	return tpl

#user input
print("Please pick an option from the following:")
print("1: Most common word")
print("2: Words occuring at least X times \n")
command = input("Your choice: ")
if command == "1":
	print(mostcommon(word_freq))
elif command == "2":
	num = input("How many times should the word repeat? : ")
	print(atleast(word_freq, int(num)))