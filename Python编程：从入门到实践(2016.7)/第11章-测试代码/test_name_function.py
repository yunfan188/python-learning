##11.1 编写单元测试函数和测试用例

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	def test_first_last_name(self):
		formatted_name = get_formatted_name('robins', 'wang')
		self.assertEqual(formatted_name, 'Robins Wang')
	def test_first_middle_last_name(self):
		formatted_name = get_formatted_name('james', 'jordan', 'michel')
		self.assertEqual(formatted_name, 'James Michel Jordan')

unittest.main()
