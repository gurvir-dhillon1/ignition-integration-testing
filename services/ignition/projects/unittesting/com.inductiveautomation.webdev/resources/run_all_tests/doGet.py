def doGet(request, session):
	import os, json, unittest, inspect, sys
	ROOT_PATH = '/usr/local/bin/ignition/data/projects/{}/ignition/script-python/unittests'.format(system.util.getProjectName())
	if ROOT_PATH not in sys.path:
		sys.path.insert(0, ROOT_PATH)

	loader = unittest.TestLoader()
	suite = loader.discover(start_dir=ROOT_PATH, pattern='code.py')

	class JsonTestResult(unittest.TextTestResult):
		def __init__(self, *args, **kwargs):
			super(JsonTestResult, self).__init__(*args, **kwargs)
			self.results = []
		def addSuccess(self, test):
			super(JsonTestResult, self).addSuccess(test)
			self.results.append({'test': str(test), 'status': 'success'})
		def addFailure(self, test, err):
			super(JsonTestResult, self).addFailure(test, err)
			self.results.append({
				'test': str(test),
				'status': 'failure',
				'error': self._exc_info_to_string(err, test)
			})
		def addError(self, test, err):
			super(JsonTestResult, self).addError(test, err)
			self.results.append({
				'test': str(test),
				'status': 'error',
				'error': self._exc_info_to_string(err, test)			
			})

	runner = unittest.TextTestRunner(resultclass=JsonTestResult)
	result = runner.run(suite)

	successes = sum(1 for res in result.results if res['status'] == 'success')
	failures = sum(1 for res in result.results if res['status'] == 'failure')
	errors = sum(1 for res in result.results if res['status'] == 'error')

	res = {
		'successes': successes,
		'failures': failures,
		'errors': errors,
		'all_tests': result.results
	}

	return {
		'contentType': 'application/json',
		'response': json.dumps(res, indent=2)
	}