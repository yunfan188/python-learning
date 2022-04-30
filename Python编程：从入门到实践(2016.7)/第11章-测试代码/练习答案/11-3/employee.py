# 定义Employee类

class Employee():
	def __init__(self, f_name, l_name, salary=5000):
		#初始化employee
		self.f_name = f_name.title()
		self.l_name = l_name.title()
		self.salary = salary

	def give_raise(self, amount=5000):
		self.salary += amount
