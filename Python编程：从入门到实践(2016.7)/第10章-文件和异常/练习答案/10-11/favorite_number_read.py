import json

filename = "favorite_number.json"
try:
	with open(filename, "r") as f_obj:
		number = json.load(f_obj)
except FileNotFoundError:
	print("Sorry, the file: "+ filename+ " not exist!")
else:
	print("I know your favorite number! It`s "+ str(number)+ ".")
