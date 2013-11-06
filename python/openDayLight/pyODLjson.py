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
setFlow = url + 'flowprogrammer/{containerName}/node/{nodeType}/{nodeId}/staticFlow/{name}'
switchId = list()
nodeType = list()
responses = list()

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

def getNodeTypes(dataDict):
        mylist = dataDict['flowStatistics']
        for i in range(len(mylist)):
                mylist1 =  mylist[i]
                nodeType.insert(i, mylist1['node']['type'])
        return nodeType

print (getSwitchIds(data))
print (getNodeTypes(data))

def putFlow(nodeTypes, switchIds, name):
	for i in range(len(nodeTypes)):
		jsonData = ''
		req = urllib2.Request(url + '/flowprogrammer/default/node/' + nodeTypes[i] + '/' + switchIds[i] + '/staticFlow/' + name + i + '/')
		req.add_header('Content-Type', 'application/json')
		response = urllib2.urlopen(req, json.dumps(jsonData))
		responses.insert(i, response)
	return responses

print (putFlow(getNodeTypes(data), getSwitchIds(data), 'mike'))
