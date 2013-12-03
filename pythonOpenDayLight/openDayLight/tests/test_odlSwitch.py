'''
Created on Nov 14, 2013

@author: mikeoutland
'''
import unittest
from pythonOpenDayLight.openDayLight import odlSwitch


class Test(unittest.TestCase):

    defaultFlowStatJson={}
    switchList = []
    typeList = []
    testBaseUrl = 'http://ec2-54-202-78-146.us-west-2.compute.amazonaws.com:8080/controller/nb/v2/'
    
    def setUp(self):
        self.defaultFlowStatJson = {u'flowStatistics': [{u'node': {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:01'}, u'flowStatistic': []}]}
        self.switchList = [u'00:00:00:00:00:00:00:01']
        self.typeList = [u'OF']
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
        switch = odlSwitch.odlSwitch(self.testBaseUrl)
        self.assertEquals(switch.putFlow(switch.getNodeTypes(self.defaultFlowStatJson)[0], switch.getSwitchIds(self.defaultFlowStatJson)[0], 'flow0', '10.0.0.1', 1, 2), 'Success')

    def testRemoveFlow(self):
        switch = odlSwitch.odlSwitch(self.testBaseUrl)
        switch.putFlow(switch.getNodeTypes(self.defaultFlowStatJson)[0], switch.getSwitchIds(self.defaultFlowStatJson)[0], 'flow0', '10.0.0.1', 1, 2)
        self.assertEquals(switch.removeFlow(switch.getNodeTypes(self.defaultFlowStatJson)[0], switch.getSwitchIds(self.defaultFlowStatJson)[0], 'flow0'), '')

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetSwitchIds']
    unittest.main()