'''
Created on Dec 4, 2013

@author: mikeoutland
'''
import json

class odlJson(object):
    
    flowName =''
    switchId = ''
    switchType = 'OF'
    inPort = 0
    outPort = 0
    
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
        
    def addAction(self, action):
        self.action.append(action)
        
    def setHostId(self, hostId):
        self.hostId = hostId
        
    def getHostId(self):
        return self.hostId
        
    def setHostType(self, hostType):
        self.hostType = hostType
        
    def getHostType(self):
        return self.hostType
        
    def setVlan(self, vlan):
        self.vlan = vlan
        
    def getVlan(self):
        return self.vlan
        
    def setHostIp(self, hostIp):
        self.hostIp = hostIp
        
    def getHostIp(self):
        return self.hostIp
    
    def setNodeId(self, nodeId):
        self.nodeId = nodeId
        
    def getNodeId(self):
        return self.nodeId
    
    def setTopoName(self, topoName):
        self.topoName = topoName
        
    def getTopoName(self):
        return self.topoName
    
    def setSrcNode(self, switchMac):
        self.srcNode = switchMac
        
    def getSrcNode(self):
        return self.srcNode
    
    def setDstNode(self, switchMac):
        self.dstNode = switchMac
        
    def getDstNode(self):
        return self.dstNode
        
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
                "actions":self.action
                }
        
    def buildPutHostJson(self):
        self.jsonData = {
 "dataLayerAddress":self.hostId,
 "nodeType":self.switchType,
 "nodeId":self.switchId,
 "nodeConnectorType":self.hostType,
 "nodeConnectorId":self.nodeId,
 "vlan":self.vlan,
 "staticHost":"true",
 "networkAddress":self.hostIp
}
        
    def buildPutTopoJson(self):
        self.jsonData = {
"status":"Success",
"name":self.topoName,
"srcNodeConnector":"OF|2@OF|" + self.srcNode,
"dstNodeConnector":"OF|2@OF|" + self.dstNode
}
        
    def __init__(self):
        self.flowName = ''
        self.switchId = ''
        self.switchType = 'OF'
        self.hostType = 'OF'
        self.hostId = ''
        self.nodeId = 1
        self.inPort = 0
        self.action = list()
        self.vlan = 1

        
    @classmethod    
    def odlJsonFlow(cls, name):
        obj = cls()
        obj.flowName = name
        obj.switchId = ''
        obj.switchType = 'OF'
        obj.hostType = 'OF'
        obj.hostId = ''
        obj.nodeId = 1
        obj.inPort = 0
        obj.action = list()
        obj.vlan = 1
        return obj
        
    @classmethod
    def odlJsonHost(cls, hostIp):
        obj = cls()
        obj.hostIp = hostIp
        obj.switchId = ''
        obj.switchType = 'OF'
        obj.hostType = 'OF'
        obj.hostId = ''
        obj.nodeId = 1
        obj.inPort = 0
        obj.action = list()
        obj.vlan = 1
        return obj
    
    @classmethod
    def odlJsonTopo(cls, topoName):
        obj = cls()
        obj.topoName = topoName
        obj.switchId = ''
        obj.srcNode = ''
        obj.dstNode = ''
        obj.hostId = ''
        obj.nodeId = 1
        obj.inPort = 0
        obj.action = list()
        obj.vlan = 1
        return obj