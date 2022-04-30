"""
# 11.2.4 setUp()方法
#程序描述：使用setUp()来创建一个调查对象和一组答案，供两个测试方法使用。
# 当unittest.TestCase类包含方法setUp(),那么可以只需要创建被测试对象实例一次，就可以在每个测试方法中使用它们。如果你在TestCase类中包含了方
法setUp(),Python将先运行setUp()方法，然后在运行各个以test_打头的测试方法。如此，在你编写的每个测试用例中都可以使用在setUp()方法中创建的对
象。
"""

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	#创建一个调查对象和一组答案，供测试的方法使用
	def setUp(self):
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question) #创建对象实例,self关键字不能省
		self.responses = ["Chinese", "English", "Spanish"]
	
	#针对AnonymousSurvey类的测试
	def test_store_single_response(self):
		#测试单个答案会被妥善地存储
		#question = "What language did you first learn to speak?"
		#my_survey = AnonymousSurvey(question) #创建对象实例
		#my_survey.store_response("Chinese")
		self.my_survey.store_response(self.responses[0])
		self.assertIn("Chinese", self.my_survey.responses)

	def test_store_three_resposes(self):
		#测试3个答案会被妥善地存储
		#question = "What language did you first learn to speak?"
		#my_survey = AnonymousSurvey(question) #创建对象实例
		#responses = ["Chinese", "English", "Spanish"]
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)

unittest.main()
