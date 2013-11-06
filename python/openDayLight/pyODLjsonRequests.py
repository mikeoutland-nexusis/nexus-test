'''
Created on Nov 6, 2013

@author: mikeoutland
'''
#!/usr/bin/python
# test app for ODL flow control in JSON
# REST api for ODL can be found here https://wiki.opendaylight.org/view/OpenDaylight_Controller:REST_Reference_and_Authentication

import json
import requests


url = 'http://127.0.0.1:8080/controller/nb/v2/'
top_level_url = url
user = 'admin'
password = 'admin'
auth = (user, password)
flow = url + 'statistics/default/flow'
setFlow = url + 'flowprogrammer/{containerName}/node/{nodeType}/{nodeId}/staticFlow/{name}'
switchId = list()
nodeType = list()
responses = list()

resp = requests.get(flow, auth=auth)
data = json.loads(resp.text)
print (data)


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

print (putFlow(getNodeTypes(data), getSwitchIds(data), 'flow'))