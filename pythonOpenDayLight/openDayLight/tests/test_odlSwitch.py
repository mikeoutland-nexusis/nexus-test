'''
Created on Nov 14, 2013

@author: mikeoutland
'''
import unittest
import socket
from pythonOpenDayLight.openDayLight import odlSwitch, odlJson


class Test(unittest.TestCase):

    if socket.gethostname() == 'ip-10-232-26-187':
        testBaseUrl = 'http://ec2-54-202-78-146.us-west-2.compute.amazonaws.com:8080/controller/nb/v2/'
    else:
        testBaseUrl = 'http://localhost:8080/controller/nb/v2/'
    
    def setUp(self):
        self.defaultFlowStatJson = {u'flowStatistics': [{u'node': {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:01'}, u'flowStatistic': []}]}
        self.switchList = [u'00:00:00:00:00:00:00:01']
        self.typeList = [u'OF']
        self.hostList = u'10.0.0.1'
        self.switch = odlSwitch.odlSwitch(self.testBaseUrl)
        self.switch.removeAllFlows()
        self.switch.removeAllActiveHosts()
        self.switch.removeAllTopoLinks()
        self.flow0 = odlJson.odlJson.odlJsonFlow('flow0')
        self.flow0.setInPort(1)
        self.flow0.addAction("OUTPUT=2")
        self.flow0.setSwitchId(self.switch.getSwitchIds(self.defaultFlowStatJson)[0])
        self.flow0.buildPutFlowJson()
        self.host0 = odlJson.odlJson.odlJsonHost("10.0.0.1")
        self.host0.setSwitchId(self.switch.getSwitchIds(self.defaultFlowStatJson)[0])
        self.host0.setHostId('00:00:00:00:01:01')
        self.host0.setNodeId(1)
        self.host0.buildPutHostJson()
        pass


    def tearDown(self):
        pass


    def testGetSwitchIds(self):
        switch = odlSwitch.odlSwitch(self.testBaseUrl)
        self.assertEquals(switch.getSwitchIds(self.defaultFlowStatJson), self.switchList)
        pass

    def testGetNodeTypes(self):
        switch = odlSwitch.odlSwitch(self.testBaseUrl)
        self.assertEquals(switch.getNodeTypes(self.defaultFlowStatJson), self.typeList)
        
    def testPutFlow(self):
        self.switch.removeFlow(self.flow0)
        self.assertEquals(self.switch.putFlow(self.flow0), 'Success')

    def testRemoveFlow(self):
        self.switch.putFlow(self.flow0)
        self.assertEquals(self.switch.removeFlow(self.flow0), '')
        
    def testGetFlows(self):
        self.switch.putFlow(self.flow0)
        self.assertEqual(self.switch.getFlows()[0].getName(), self.flow0.getName())
        
    def testGetActiveHosts(self):
        self.switch.putHost(self.host0)
        self.assertEquals(self.switch.getActiveHosts()[0].getHostIp(), self.hostList)
        
    def testRemoveActiveHosts(self):
        self.switch.putHost(self.host0)
        self.assertEquals(self.switch.removeHost(self.host0), '')
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetSwitchIds']
    unittest.main()