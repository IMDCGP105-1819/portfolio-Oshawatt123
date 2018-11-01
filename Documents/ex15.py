lyric = "oh dan oh why do you play TF2 you absolute baboon"

lyric_list = lyric.split(" ")
word_freq = {}

x = 0
while x < len(lyric_list):
	if lyric_list[x] in word_freq:
		word_freq[lyric_list[x]] += 1
	else:
		word_freq[lyric_list[x]] = 1
	x += 1

def mostcommon(word_freq):
	mostcommonword = []
	mostcommonwordfreq = 0
	for x in word_freq:
		if word_freq.get(x) > mostcommonwordfreq:
			mostcommonword = [x]
			mostcommonwordfreq = word_freq.get(x)
		elif word_freq.get(x) == mostcommonwordfreq:
			mostcommonword.append(x)
	tpl = (mostcommonword, mostcommonwordfreq)
	return tpl
	
def atleast(word_freq, num):
	wordlist = []
	for x in word_freq:
		if word_freq.get(x) >= num:
			wordlist.append(x)
	tpl = (wordlist, num)
	return tpl

print("Please pick an option from the following:")
print("1: Most common word")
print("2: Words occuring at least X times \n")
command = input("Your choice: ")
if command == "1":
	print(mostcommon(word_freq))
elif command == "2":
	num = input("How many times should the word repeat? : ")
	print(atleast(word_freq, int(num)))