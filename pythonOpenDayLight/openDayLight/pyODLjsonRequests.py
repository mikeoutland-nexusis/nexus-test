'''
Created on Nov 6, 2013

@author: mikeoutland
'''
#!/usr/bin/python
# test app for ODL flow control in JSON
# REST api for ODL can be found here https://wiki.opendaylight.org/view/OpenDaylight_Controller:REST_Reference_and_Authentication
# Requires requests object to be installed.  http://www.python-requests.org/en/latest/user/install/#install

import json
import requests


url = 'http://127.0.0.1:8080/controller/nb/v2/'
top_level_url = url
user = 'admin'
password = 'admin'
auth = (user, password)
flow = url + 'statistics/default/flow'

def getActiveHosts(restUrl, auth):
    response = requests.get((restUrl + "hosttracker/default/hosts/active"), auth=auth)
    return response

def getInactiveHosts(restUrl, auth):
    response = requests.get((restUrl + "hosttracker/default/hosts/inactive"), auth=auth)
    return response

def getSwitchIds(dataDict):
    switchId = list()
    mylist = dataDict['flowStatistics']
    for i in range(len(mylist)):
        mylist1 =  mylist[i]
        switchId.insert(i, mylist1['node']['id'])
    return switchId

def getNodeTypes(dataDict):
    nodeType = list()
    mylist = dataDict['flowStatistics']
    for i in range(len(mylist)):
        mylist1 =  mylist[i]
        nodeType.insert(i, mylist1['node']['type'])
    return nodeType

def putFlow(nodeTypes, switchIds, name, srcIp, inPort, outPort):
    jsonData = { 
            "installInHw":"false",
            "name": name,
            "node":{
                "id":switchIds,
                "type": nodeTypes
                },
            "ingressPort": str(inPort),
            "priority":"500",
            "nwSrc": srcIp,
            "actions":[
                    ("OUTPUT=" + str(outPort))
                    ]
            }
    requestURI = (url + 'flowprogrammer/default/node/' + nodeTypes + '/' + switchIds + '/staticFlow/' + name)
    req = requests.put(requestURI, data = json.dumps(jsonData),  headers = {'Content-Type': 'application/json'}, auth=auth)
    return req.text


resp = requests.get(flow, auth=auth)
data = json.loads(resp.text)
print (data)
print (getSwitchIds(data))
print (putFlow(getNodeTypes(data)[0], getSwitchIds(data)[0], 'flow0', '10.0.0.1', 1, 2))
print (putFlow(getNodeTypes(data)[0], getSwitchIds(data)[0], 'flow1', '10.0.0.2', 2, 1))
data = json.loads(getActiveHosts(url, auth).text)
print (data)
data = json.loads(getInactiveHosts(url, auth).text)
print (data)
