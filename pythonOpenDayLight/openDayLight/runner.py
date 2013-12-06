'''
Created on Nov 14, 2013

@author: mikeoutland
'''

#In mininet i'm using the following config:
#    mn --topo single,3 --mac --switch ovsk --controller=remote,ip=10.0.2.2,port=6633
#    The current runner will setup a simple flow between h1 and h2 

import socket
import sys
from pythonOpenDayLight.openDayLight import odlSwitch, odlJson

if len(sys.argv) > 1:
    if (sys.argv[1] == "prod"):
        testBaseUrl = 'http://ec2-54-202-188-17.us-west-2.compute.amazonaws.com:8080/controller/nb/v2/'
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
host4json = odlJson.odlJson('h1tomore')
host5json = odlJson.odlJson('h2tomore')
host6json = odlJson.odlJson('h3tomore')
host7json = odlJson.odlJson('s1toallsw')

host1json.setSwitchId(switch.getSwitchIds(data)[0])
host2json.setSwitchId(switch.getSwitchIds(data)[1])
host3json.setSwitchId(switch.getSwitchIds(data)[2])
host4json.setSwitchId(switch.getSwitchIds(data)[0])
host5json.setSwitchId(switch.getSwitchIds(data)[1])
host6json.setSwitchId(switch.getSwitchIds(data)[2])
host7json.setSwitchId(switch.getSwitchIds(data)[0])

host1json.setInPort(1)
host1json.addAction("OUTPUT=2")
host1json.addAction("OUTPUT=3")
host1json.buildPutFlowJson()

host2json.setInPort(1)
host2json.addAction("OUTPUT=2")
host2json.buildPutFlowJson()

host3json.setInPort(1)
host3json.addAction("OUTPUT=2")
host3json.buildPutFlowJson()

host4json.setInPort(2)
host4json.addAction("OUTPUT=1")
host4json.addAction("OUTPUT=3")
host4json.buildPutFlowJson()

host5json.setInPort(2)
host5json.addAction("OUTPUT=1")
host5json.buildPutFlowJson()

host6json.setInPort(2)
host6json.addAction("OUTPUT=1")
host6json.buildPutFlowJson()

host7json.setInPort(3)
host7json.addAction("OUTPUT=1")
host7json.addAction("OUTPUT=2")
host7json.buildPutFlowJson()

print (switch.getSwitchIds(data))

print (switch.putFlow(host1json))
print (switch.putFlow(host2json))
print (switch.putFlow(host3json))
print (switch.putFlow(host4json))
print (switch.putFlow(host5json))
print (switch.putFlow(host6json))
print (switch.putFlow(host7json))


print (switch.getFlowStatJson())
