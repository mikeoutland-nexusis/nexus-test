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

def putFlow(nodeTypes, switchIds, name):
    responses = list()
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
        req = requests.put(requestURI, data = json.dumps(jsonData),  headers = {'Content-Type': 'application/json'}, auth=auth)
        print (requestURI)
        print (json.dumps(jsonData))
        responses.insert(i, req.text)


    return responses


resp = requests.get(flow, auth=auth)
data = json.loads(resp.text)
print (data)
print (getSwitchIds(data))
print (getNodeTypes(data))
print (putFlow(getNodeTypes(data), getSwitchIds(data), 'flow'))
