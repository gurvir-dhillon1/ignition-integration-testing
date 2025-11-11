import unittest, cStringIO
def run_test_suite(test_class):
	loader = unittest.TestLoader()
	suite = loader.loadTestsFromTestCase(test_class)
	
	buf = cStringIO.StringIO()
	runner = unittest.TextTestRunner(stream=buf, verbosity=2)
	result = runner.run(suite)
	
	return {
		'class': test_class.__name__,
		'total': result.testsRun,
		'failures': len(result.failures),
		'errors': len(result.errors),
		'success': result.wasSuccessful(),
		'output': buf.getvalue()
	}
