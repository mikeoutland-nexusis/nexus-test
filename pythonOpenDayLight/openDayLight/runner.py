'''
Created on Nov 14, 2013

@author: mikeoutland
'''

#In mininet i'm using the following config:
#    mn --topo single,3 --mac --switch ovsk --controller=remote,ip=10.0.2.2,port=6633
#    The current runner will setup a simple flow between h1 and h2 
#  adding new flow
#  ading a new comment

import socket
import sys
from pythonOpenDayLight.openDayLight import odlSwitch, odlJson

if len(sys.argv) > 1:
    if (sys.argv[1] == "prod"):
        testBaseUrl = 'http://ec2-54-202-78-146.us-west-2.compute.amazonaws.com:8080/controller/nb/v2/'
    else:
        testBaseUrl = sys.argv[1]
elif socket.gethostname() == 'ip-10-232-26-187':
    testBaseUrl = 'http://ec2-54-202-78-146.us-west-2.compute.amazonaws.com:8080/controller/nb/v2/'
else:
    testBaseUrl = 'http://localhost:8080/controller/nb/v2/'

switch = odlSwitch.odlSwitch(testBaseUrl)
switch.removeAllFlows()
data = switch.getFlowStatJson()
host1json = odlJson.odlJson('h1toall')
host2json = odlJson.odlJson('h2toall')
host3json = odlJson.odlJson('h3toall')
host4json = odlJson.odlJson('h4toall')
host1json.setInPort(1)
host1json.addAction("OUTPUT=2")
host1json.addAction("OUTPUT=3")
host1json.addAction("OUTPUT=4")
host2json.setInPort(2)
host2json.addAction("OUTPUT=1")
host2json.addAction("OUTPUT=3")
host2json.addAction("OUTPUT=4")
host3json.setInPort(3)
host3json.addAction("OUTPUT=2")
host3json.addAction("OUTPUT=1")
host3json.addAction("OUTPUT=4")
host4json.setInPort(4)
host4json.addAction("OUTPUT=2")
host4json.addAction("OUTPUT=1")
host4json.addAction("OUTPUT=3")
host1json.setSwitchId(switch.getSwitchIds(data)[0])
host2json.setSwitchId(switch.getSwitchIds(data)[0])
host3json.setSwitchId(switch.getSwitchIds(data)[0])
host4json.setSwitchId(switch.getSwitchIds(data)[0])
host1json.buildPutFlowJson()
host2json.buildPutFlowJson()
host3json.buildPutFlowJson()
host4json.buildPutFlowJson()
print (data)
print (switch.getSwitchIds(data))
print (switch.putFlow(host1json))
print (switch.putFlow(host2json))
print (switch.putFlow(host3json))
print (switch.putFlow(host4json))

#print (switch.putFlow(switch.getNodeTypes(data)[0], switch.getSwitchIds(data)[0], 'h1toh2', 1, 2))
#print (switch.putFlow(switch.getNodeTypes(data)[0], switch.getSwitchIds(data)[0], 'h2toh1', 2, 1))
print (switch.getActiveHosts())
print (switch.getInactiveHosts())
print (switch.getFlowStatJson())



#print (switch.removeFlow(switch.getNodeTypes(data)[0], switch.getSwitchIds(data)[0], 'flow0'))
#print (switch.removeFlow(switch.getNodeTypes(data)[0], switch.getSwitchIds(data)[0], 'flow1'))
