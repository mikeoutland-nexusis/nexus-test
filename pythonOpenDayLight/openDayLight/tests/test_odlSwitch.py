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
        self.switch = odlSwitch.odlSwitch(self.testBaseUrl)
        self.switch.removeAllFlows()
        self.flow0 = odlJson.odlJson('flow0')
        self.flow0.setInPort(1)
        self.flow0.setOutPort(2)
        self.flow0.setSwitchId(self.switch.getSwitchIds(self.defaultFlowStatJson)[0])
        self.flow0.buildPutFlowJson()
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
        self.assertEquals(self.switch.putFlow(self.flow0), 'Success')

    def testRemoveFlow(self):
        self.switch.putFlow(self.flow0)
        self.assertEquals(self.switch.removeFlow(self.flow0), '')

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetSwitchIds']
    unittest.main()