def getTagValue():
	return system.tag.readBlocking(['test tag'])[0].value
	
def getTag5Value():
	return system.tag.readBlocking(['always returns 5'])[0].value