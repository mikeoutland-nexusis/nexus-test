'''
Created on Nov 14, 2013

@author: mikeoutland
'''

#In mininet i'm using the following config:
#    mn --topo single,3 --mac --switch ovsk --controller=remote,ip=10.0.2.2,port=6633
#testing new gerrit another small change

from pythonOpenDayLight.openDayLight import odlSwitch

switch = odlSwitch.odlSwitch('http://127.0.0.1:8080/controller/nb/v2/')
data = switch.getFlowStatJson()
print (data)
print (switch.getSwitchIds(data))
print (switch.putFlow(switch.getNodeTypes(data)[0], switch.getSwitchIds(data)[0], 'flow0', '10.0.0.1', 1, 2))
print (switch.putFlow(switch.getNodeTypes(data)[0], switch.getSwitchIds(data)[0], 'flow1', '10.0.0.2', 2, 1))

#print (switch.removeFlow(switch.getNodeTypes(data)[0], switch.getSwitchIds(data)[0], 'flow0'))
#print (switch.removeFlow(switch.getNodeTypes(data)[0], switch.getSwitchIds(data)[0], 'flow1'))