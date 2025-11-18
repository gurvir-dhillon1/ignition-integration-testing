import unittest
import TestableFunctionsTwo
from java.lang import Integer, Double, Boolean, String

class TestTestableFunctionsTwo(unittest.TestCase):

	def testAddTwoTags(self):
		value = TestableFunctionsTwo.addTwoTags()
		self.assertIsNotNone(value, 'expected a value but got none')
		self.assertIsInstance(value, (int, float))