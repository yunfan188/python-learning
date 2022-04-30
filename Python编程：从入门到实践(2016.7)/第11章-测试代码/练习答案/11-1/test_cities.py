## 编写测试函数

import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
	def test_city_country(self):
		sz_cn = city_country('shenzhen', 'china')
		self.assertEqual(sz_cn, 'Shenzhen, China')

unittest.main()
