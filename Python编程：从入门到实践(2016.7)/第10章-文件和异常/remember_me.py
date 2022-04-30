##10.4.2 保存和读取用户生成的数据
# 1.使用json格式保存用户生成的数据
# 2.从json文件中读取数据到内存中

import json

filename = "username.json"
try:
	with open(filename, "r") as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input("What`s your name? ")
	with open(filename, "w") as f_obj:
		json.dump(username, f_obj)
		print("We`ll remember you when you come back, "+ username+ "!")
else:
	print("Welcome back, "+ username+ "!")
