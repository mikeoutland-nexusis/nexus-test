'''
Created on Nov 14, 2013

@author: mikeoutland
'''
import json
import requests
import odlJson

class odlSwitch:
    '''
    classdocs
    '''
    data = ''
    url = ''
    auth = ('','')
    
    
    def getFlowStatJson(self):
        return self.data
    
    def getActiveHosts(self):
        response = requests.get((url + "hosttracker/default/hosts/active"), auth=auth)
        dataDict = json.loads(response.text)
        hosts = list()
        mylist = dataDict['hostConfig']
        for i in range(len(mylist)):
            mylist1 =  mylist[i]
            myOdl = odlJson.odlJson.odlJsonHost(mylist1['networkAddress'])
            hosts.insert(i, myOdl)
        return hosts

    def getInactiveHosts(self):
        response = requests.get((url + "hosttracker/default/hosts/inactive"), auth=auth)
        dataDict = json.loads(response.text)
        hosts = list()
        mylist = dataDict['hostConfig']
        for i in range(len(mylist)):
            mylist1 =  mylist[i]
            myOdl = odlJson.odlJson.odlJsonHost(mylist1['networkAddress'])
            hosts.insert(i, myOdl)
        return hosts
    
    def removeAllActiveHosts(self):
        flowsList = self.getActiveHosts()
        for i in range(len(flowsList)):
            self.removeHost(flowsList[i])
    
    def getFlows(self):
        flowList = list()
        response = requests.get((url+ "flowprogrammer/default"), auth=auth)
        flowData = json.loads(response.text)
        mylist = flowData["flowConfig"]
        for i in range(len(mylist)):
            mylist1 = mylist[i]
            myOdl = odlJson.odlJson.odlJsonFlow(mylist1['name'])
            myOdl.setSwitchId(mylist1['node']['id'])
            myOdl.setSwitchType(mylist1['node']['type'])
            flowList.insert(i, myOdl)
        return flowList
    
    def removeAllFlows(self):
        flowsList = self.getFlows()
        for i in range(len(flowsList)):
            self.removeFlow(flowsList[i])
            
    
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
    
    def putFlow(self, odlJson):
        requestURI = (url + 'flowprogrammer/default/node/' + odlJson.getSwitchType() + '/' + odlJson.getSwitchId() + '/staticFlow/' + odlJson.getName())
        req = requests.put(requestURI, data = odlJson.getJson(),  headers = {'Content-Type': 'application/json'}, auth=auth)
        return req.text
    
    def putHost(self, odlJson):
        requestURI = (url + 'hosttracker/default/address/' + odlJson.getHostIp())
        req = requests.put(requestURI, data = odlJson.getJson(),  headers = {'Content-Type': 'application/json'}, auth=auth)
        return req.text
    
    def removeFlow(self, odlJson):
        requestURI = (url + 'flowprogrammer/default/node/' + odlJson.getSwitchType() + '/' + odlJson.getSwitchId() + '/staticFlow/' + odlJson.getName())
        req = requests.delete(requestURI, headers = {'Content-Type': 'application/json'}, auth=auth)
        return req.text
    
    def removeHost(self, odlJson):
        requestURI = (url + 'hosttracker/default/address/' + odlJson.getHostIp())
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

        
