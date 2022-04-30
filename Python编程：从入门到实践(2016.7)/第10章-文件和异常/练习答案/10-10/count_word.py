filenames = ['text.txt']
word = input('Input the word: ')

for filename in filenames:
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		print('Sorry, the file '+ filename+ ' doesn`t exist!')
	else:
		count = contents.lower().count(word.lower())
		print('The count of "'+ word+ '" in the '+ filename+ ': '+ str(count))
	print()
