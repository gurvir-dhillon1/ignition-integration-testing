def doGet(request, session):
	import json, unittest, os, importlib
	url_params = request.get('params')
	test_file = url_params.get('test_file')
	ROOT_PATH = unittests.TestRunner.ROOT_PATH
	if not test_file or '/' in test_file or '\\' in test_file:
		return {
			'contentType': 'text/plain',
			'response': 'no valid test file (check test_file url parameter is not empty and does not contain \'/\' or \'\\\')'
		}

	test_file_path = os.path.join(ROOT_PATH, test_file)
	if ROOT_PATH not in sys.path:
		sys.path.insert(0, ROOT_PATH)

	module_name = 'unittests.{0}'.format(test_file)

	try:
		module = importlib.import_module(module_name)
	except ImportError as e:
		return {
			'contentType': 'text/plain',
			'response': 'unable to import module {0}: {1}'.format(module_name, str(e))
		}

	loader = unittest.TestLoader()
	suite = loader.loadTestsFromModule(module)
	
	runner = unittest.TextTestRunner(resultclass=unittests.TestRunner.JsonTestResult, verbosity=2)
	result = runner.run(suite)

	res = unittests.TestRunner.generate_result_object(result)
	res['requestedModule'] = module_name

	return {
		'contentType': 'application/json',
		'response': json.dumps(res, indent=2)
	}