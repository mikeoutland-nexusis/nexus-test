#!/usr/bin/python
# test app for ODL flow control in JSON
# REST api for ODL can be found here https://wiki.opendaylight.org/view/OpenDaylight_Controller:REST_Reference_and_Authentication

import json
import urllib2
from urllib2 import Request, urlopen, URLError, HTTPError


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

def basic_authorization(user, password):
	s = user + ":" + password
	return "Basic " + s.encode("base64").rstrip()

def putFlow(nodeTypes, switchIds, name):
	for i in range(len(nodeTypes)):
		jsonData = { 
				"installInHw":"false",
				"name": name + str(i),
				"node":{
					"id":switchIds[i],
					"type": "OF"
					},
				"ingressPort":"1",
				"priority":"500",
				"etherType":"0x800",
				"nwSrc":"10.0.0.1",
				"actions":[
						"OUTPUT=2"
						]
				}
		requestURI = (url + 'flowprogrammer/default/node/' + nodeTypes[i] + '/' + switchIds[i] + '/staticFlow/' + name + str(i))
		req = urllib2.Request(requestURI, data = json.dumps(jsonData),  headers = {'Authorization': basic_authorization("Admin", "Password"), 'Content-Type': 'application/json'})
		print (requestURI)
		print (json.dumps(jsonData))
		try:
			response = urllib2.urlopen(req)
			responses.insert(i, response.read())
		except URLError as e:
			responses.insert(i, "URLError({0}): {1}".format(e.code, e.reason))

	return responses

print (putFlow(getNodeTypes(data), getSwitchIds(data), 'flow'))
