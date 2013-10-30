#!/usr/bin/python
# test app for ODL flow control in JSON

import json
import urllib2

url = 'http://127.0.0.1:8080/controller/nb/v2/'
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
top_level_url = url
user = 'admin'
password = 'admin'
flow = url + 'statistics/default/flow'
switchId = list()

password_mgr.add_password(None, top_level_url, user, password)

handler = urllib2.HTTPBasicAuthHandler(password_mgr)

opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)

data = json.load(urllib2.urlopen(flow))


def getSwitchIds(dataDict):
	mylist = dataDict['flowStatistics']
	for i in range(len(mylist)):
		mylist1 =  mylist[i]
		switchId.insert(i, mylist1['node']['id'])
	return switchId

print (getSwitchIds(data))
