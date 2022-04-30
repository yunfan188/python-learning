## 编写测试函数

import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
	def test_city_country(self):
		sz_cn = city_country('shenzhen', 'china')
		self.assertEqual(sz_cn, 'Shenzhen, China')
	def test_city_country_population(self):
		sz_cn_pl = city_country('shenzhen', 'china', 15000000)
		self.assertEqual(sz_cn_pl, "Shenzhen, China - population 15000000")

unittest.main()
