import json

filename = "favorite_number.json"
try:
	with open(filename, "r") as f_obj:
		number = json.load(f_obj)
except FileNotFoundError:
	number = input("What`s your favrite number? ")
	with open(filename, "w") as f_obj:
		json.dump(number, f_obj)
		print("Thanks! I`ll remember that.")
else:
	print("I know your favorite number! It`s "+ str(number)+ ".")
