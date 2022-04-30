# 测试Employee类中的方法

import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
	def setUp(self):
		self.Eric = Employee("Eric", "matthes", 65000)

	def test_give_default_raise(self):
		self.Eric.give_raise()
		self.assertEqual(70000, self.Eric.salary)

	def test_give_custom_raise(self):
		self.Eric.give_raise(10000)
		self.assertEqual(75000, self.Eric.salary)

unittest.main()
