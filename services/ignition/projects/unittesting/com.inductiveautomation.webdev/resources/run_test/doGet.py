def doGet(request, session):
	import json, unittest, os, importlib
	url_param_name = 'test_files'
	url_params = request.get('params')
	test_files = url_params.get(url_param_name)
	ROOT_PATH = unittests.TestRunner.ROOT_PATH
	if not test_files or '/' in test_files or '\\' in test_files:
		return {
			'contentType': 'text/plain',
			'response': 'no valid {0} (check {0} url parameter is not empty and does not contain \'/\' or \'\\\')'.format(url_param_name)
		}
	test_files = [f.strip() for f in test_files.split(',') if f.strip()]

	if ROOT_PATH not in sys.path:
		sys.path.insert(0, ROOT_PATH)

	imported_modules = []
	import_errors = {}
	loader = unittest.TestLoader()
	suite = unittest.TestSuite()

	for f in test_files:
		module_name = 'unittests.{0}'.format(f)
		try:
			module = importlib.import_module(module_name)
			suite.addTests(loader.loadTestsFromModule(module))
			imported_modules.append(module_name)
		except ImportError as e:
			import_errors[f] = str(e)
	
	runner = unittest.TextTestRunner(resultclass=unittests.TestRunner.JsonTestResult, verbosity=2)
	result = runner.run(suite)

	res = unittests.TestRunner.generate_result_object(result)
	res['requestedModule'] = imported_modules
	if import_errors:
		res['import_errors'] = import_errors

	return {
		'contentType': 'application/json',
		'response': json.dumps(res, indent=2)
	}