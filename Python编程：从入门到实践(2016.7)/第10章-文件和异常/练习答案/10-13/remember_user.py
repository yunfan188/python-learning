import json

def get_stored_username():
	filename = "username.json"
	try:
		with open(filename, "r") as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		print("The file: "+ filename+ " not exist!")
		return None
	else:
		return username

def get_new_username():
	filename = "username.json"
	username = input("what`s your name? ")
	with open(filename, "w") as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	username = get_stored_username()
	if username:
		correct = input("Are you "+ username+ "? (y/n) ")
		if correct == 'y':
			print("Welcome back, "+ username+ "!")
			return
	username = get_new_username()
	print("We`ll remember you when you come back, "+ username+ "!")

#调用greet_user()函数
greet_user()
