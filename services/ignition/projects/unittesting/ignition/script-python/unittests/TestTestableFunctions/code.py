import unittest
import TestableFunctions
from java.lang import Integer, Double, Boolean, String

class TestTestableFunctions(unittest.TestCase):
	
	def testGetTagValue(self):
		value = TestableFunctions.getTagValue()
		self.assertIsNotNone(value, 'expected a value from tag but got none')
		self.assertIsInstance(value, (int, float, str))
		print('testGetTagValue passed with:', value)
		
	def testTag5Value(self):
		value = TestableFunctions.getTag5Value()
		self.assertIsNotNone(value, 'expected a value from tag but got none')
		self.assertIsInstance(value, (int, float, str))
		self.assertTrue(Integer(5).equals(value), 'expected tag value 5 but got {}'.format(value))