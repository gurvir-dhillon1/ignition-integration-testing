def getTagValue():
	return system.tag.readBlocking(['test tag'])[0].value