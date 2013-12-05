'''
Created on Dec 4, 2013

@author: mikeoutland
'''
import json

class odlJson:
    
    flowName =''
    switchId = ''
    switchType = 'OF'
    inPort = 0
    outPort = 0
    jsonData = {''}
    
    def setName(self, name):
        self.flowName = name
        
    def getName(self):
        return self.flowName
        
    def setSwitchId(self, switchId):
        self.switchId = switchId
        
    def getSwitchId(self):
        return self.switchId
        
    def setSwitchType(self, switchType):
        self.switchType = switchType
        
    def getSwitchType(self):
        return self.switchType
        
    def setInPort(self, port):
        self.inPort = port
        
    def setOutPort(self, port):
        self.outPort = port
        
    def getJson(self):
        return json.dumps(self.jsonData)
    
    def buildPutFlowJson(self):
        self.jsonData = { 
                "installInHw":"true",
                "name": self.flowName,
                "node":{
                    "id":self.switchId,
                    "type": self.switchType
                    },
                "ingressPort": str(self.inPort),
                "priority":"500",
                "actions":[
                        ("OUTPUT=" + str(self.outPort))
                        ]
                }
        
    def __init__(self):
        self.flowName =''
        self.switchId = ''
        self.switchType = 'OF'
        self.inPort = 0
        self.outPort = 0
        self.jsonData = {''}