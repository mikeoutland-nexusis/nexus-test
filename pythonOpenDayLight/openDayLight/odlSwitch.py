'''
Created on Nov 14, 2013

@author: mikeoutland
'''
import json
import requests

class odlSwitch:
    '''
    classdocs
    '''
    data = ''
    url = ''
    auth = ('','')
    
    
    def getFlowStatJson(self):
        return self.data
    
    def getActiveHosts(self, restUrl, auth):
        response = requests.get((restUrl + "hosttracker/default/hosts/active"), auth=auth)
        return response

    def getInactiveHosts(self, restUrl, auth):
        response = requests.get((restUrl + "hosttracker/default/hosts/inactive"), auth=auth)
        return response
    
    def getSwitchIds(self, dataDict):
        switchId = list()
        mylist = dataDict['flowStatistics']
        for i in range(len(mylist)):
            mylist1 =  mylist[i]
            switchId.insert(i, mylist1['node']['id'])
        return switchId
    
    def getNodeTypes(self, dataDict):
        nodeType = list()
        mylist = dataDict['flowStatistics']
        for i in range(len(mylist)):
            mylist1 =  mylist[i]
            nodeType.insert(i, mylist1['node']['type'])
        return nodeType
    
    def putFlow(self, nodeTypes, switchIds, name, srcIp, inPort, outPort):
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
    
    def removeFlow(self, nodeTypes, switchIds, name):
        requestURI = (url + 'flowprogrammer/default/node/' + nodeTypes + '/' + switchIds + '/staticFlow/' + name)
        req = requests.delete(requestURI, headers = {'Content-Type': 'application/json'}, auth=auth)
        return req.text


    def __init__(self, baseUrl):
        '''
        Constructor
        ''' 
        global url
        global auth
        url = baseUrl
        user = 'admin'
        password = 'admin' 
        auth = (user, password)
        flow = url + 'statistics/default/flow'
        resp = requests.get(flow, auth=auth)
        self.data = json.loads(resp.text)

        