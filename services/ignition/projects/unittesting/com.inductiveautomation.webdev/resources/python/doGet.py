def doGet(request, session):
	import os, json
	static_path = unittests.CONSTANTS.ROOT_PATH
	all_test_files = []
	for root, dirs, files in os.walk(static_path):
		dir_name = os.path.basename(root).lower()
		if dir_name.startswith('test') or dir_name.endswith('test'):
			code_path = os.path.join(root, 'code.py')
			if os.path.exists(code_path):
				all_test_files.append(code_path)
				
	all_results = []
	
	for path in all_test_files:
		local_scope = {}
		try:
			execfile(path, local_scope)
			if 'run_tests' in local_scope:
				try:
					result = local_scope['run_tests']()
					all_results.append(result)
				except Exception as e:
					all_results.append({'class': dir_name, 'error': str(e)})
			else:
				all_results.append({'class': dir_name, 'error': 'no run_tests() found'})
		except Exception as e:
			all_results.append('error in {}: {}'.format(path, str(e)))
			
	successes, failures, errors = 0, 0, 0
	
	for data in all_results:
		if not isinstance(data, dict):
			continue
		successes += 1 if data.get('success') else 0
		failures += data.get('failures', 0)
		errors += data.get('errors', 0)
	
	res = {
		'successes': successes,
		'failures': failures,
		'errors': errors,
		'all_tests': all_results
	}
	return {
		'contentType': 'application/json',
		'response': json.dumps(res, indent=2)
	}