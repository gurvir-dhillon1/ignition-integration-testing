def doGet(request, session):
	import os, json, unittest, inspect, sys
	ROOT_PATH = unittests.TestRunner.ROOT_PATH
	if ROOT_PATH not in sys.path:
		sys.path.insert(0, ROOT_PATH)

	loader = unittest.TestLoader()
	suite = loader.discover(start_dir=ROOT_PATH, pattern='code.py')

	runner = unittest.TextTestRunner(resultclass=unittests.TestRunner.JsonTestResult, verbosity=2)
	result = runner.run(suite)

	res = unittests.TestRunner.generate_result_object(result)

	return {
		'contentType': 'application/json',
		'response': json.dumps(res, indent=2)
	}