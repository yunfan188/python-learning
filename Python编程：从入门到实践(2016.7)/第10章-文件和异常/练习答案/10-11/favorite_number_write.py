import json

filename = "favorite_number.json"
number = input("What`s your favrite number? ")
with open(filename, "w") as f_obj:
	json.dump(number, f_obj)
	print("Thanks! I`ll remember that.")
