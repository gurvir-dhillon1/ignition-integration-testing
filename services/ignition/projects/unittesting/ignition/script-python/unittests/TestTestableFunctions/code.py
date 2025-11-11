import unittest
import TestableFunctions
class TestTestableFunctions(unittest.TestCase):
	
	def testGetTagValue(self):
		value = TestableFunctions.getTagValue()
		self.assertIsNotNone(value, 'expected a value from tag but got none')
		self.assertIsInstance(value, (int, float, str))
		print('testGetTagValue passed with:', value)
		
def run_tests():
	loader = unittest.TestLoader()
	suite = loader.loadTestsFromTestCase(TestTestableFunctions)
	
	import cStringIO
	buf = cStringIO.StringIO()
	runner = unittest.TextTestRunner(stream=buf, verbosity=2)
	result = runner.run(suite)
	
	summary = {
		'class': 'TestTestableFunctions',
		'total': result.testsRun,
		'failures': len(result.failures),
		'errors': len(result.errors),
		'success': result.wasSuccessful(),
		'output': buf.getvalue()
	}
	return summary