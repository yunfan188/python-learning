filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		pass
	else:
		print('\nReading file: '+ filename)
		print(contents.rstrip())
