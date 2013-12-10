'''
Created on Nov 14, 2013

@author: mikeoutland
'''

#In mininet i'm using the following config:
#    mn --custom custom/topo3Sw2HostPer.py --topo ThreeSwTwoHostPerTopo --mac --switch ovsk --controller=remote,ip=10.0.2.2,port=6633


import socket
import sys
from pythonOpenDayLight.openDayLight import odlSwitch, odlJson

if len(sys.argv) > 1:
    if (sys.argv[1] == "prod"):
        testBaseUrl = 'http://ec2-54-202-188-17.us-west-2.compute.amazonaws.com:8080/controller/nb/v2/'
    else:
        testBaseUrl = sys.argv[1]
elif socket.gethostname() == 'ip-10-232-26-187':
    testBaseUrl = 'http://ec2-54-245-68-94.us-west-2.compute.amazonaws.com:8080/controller/nb/v2/'
else:
    testBaseUrl = 'http://localhost:8080/controller/nb/v2/'

switch = odlSwitch.odlSwitch(testBaseUrl)
switch.removeAllFlows()
switch.removeAllActiveHosts()
switch.removeAllTopoLinks()
data = switch.getFlowStatJson()
flow1json = odlJson.odlJson.odlJsonFlow('h1toh2s2')
flow2json = odlJson.odlJson.odlJsonFlow('h2toh1s2')
flow3json = odlJson.odlJson.odlJsonFlow('h3tos1')
flow4json = odlJson.odlJson.odlJsonFlow('h4tos3')
flow5json = odlJson.odlJson.odlJsonFlow('h5toh6s2')
flow6json = odlJson.odlJson.odlJsonFlow('h6toh5s2')
flow7json = odlJson.odlJson.odlJsonFlow('s1toh3')
flow8json = odlJson.odlJson.odlJsonFlow('s3toh4')
flow9json = odlJson.odlJson.odlJsonFlow('s2toh1h2')
flow10json = odlJson.odlJson.odlJsonFlow('s2toh5h6')

host1 = odlJson.odlJson.odlJsonHost("10.0.0.1")
host2 = odlJson.odlJson.odlJsonHost("10.0.0.2")
host3 = odlJson.odlJson.odlJsonHost("10.0.0.3")
host4 = odlJson.odlJson.odlJsonHost("10.0.0.4")
host5 = odlJson.odlJson.odlJsonHost("10.0.0.5")
host6 = odlJson.odlJson.odlJsonHost("10.0.0.6")

topo1 = odlJson.odlJson.odlJsonTopo("link1")
topo2 = odlJson.odlJson.odlJsonTopo("link2")

flow1json.setSwitchId(switch.getSwitchIds(data)[2])
flow2json.setSwitchId(switch.getSwitchIds(data)[2])
flow3json.setSwitchId(switch.getSwitchIds(data)[0])
flow4json.setSwitchId(switch.getSwitchIds(data)[0])
flow5json.setSwitchId(switch.getSwitchIds(data)[1])
flow6json.setSwitchId(switch.getSwitchIds(data)[1])
flow7json.setSwitchId(switch.getSwitchIds(data)[0])
flow8json.setSwitchId(switch.getSwitchIds(data)[0])
flow9json.setSwitchId(switch.getSwitchIds(data)[2])
flow10json.setSwitchId(switch.getSwitchIds(data)[1])

flow1json.setInPort(1)
flow1json.addAction("OUTPUT=2")
flow1json.addAction("OUTPUT=3")
flow1json.buildPutFlowJson()

flow2json.setInPort(2)
flow2json.addAction("OUTPUT=1")
flow2json.addAction("OUTPUT=3")
flow2json.buildPutFlowJson()

flow3json.setInPort(1)
flow3json.addAction("OUTPUT=3")
flow3json.buildPutFlowJson()

flow4json.setInPort(2)
flow4json.addAction("OUTPUT=4")
flow4json.buildPutFlowJson()

flow5json.setInPort(1)
flow5json.addAction("OUTPUT=2")
flow5json.addAction("OUTPUT=3")
flow5json.buildPutFlowJson()

flow6json.setInPort(2)
flow6json.addAction("OUTPUT=1")
flow6json.addAction("OUTPUT=3")
flow6json.buildPutFlowJson()

flow7json.setInPort(3)
flow7json.addAction("OUTPUT=1")
flow7json.buildPutFlowJson()

flow8json.setInPort(4)
flow8json.addAction("OUTPUT=2")
flow8json.buildPutFlowJson()

flow9json.setInPort(3)
flow9json.addAction("OUTPUT=1")
flow9json.addAction("OUTPUT=2")
flow9json.buildPutFlowJson()

flow10json.setInPort(3)
flow10json.addAction("OUTPUT=1")
flow10json.addAction("OUTPUT=2")
flow10json.buildPutFlowJson()

print (switch.putFlow(flow1json))
print (switch.putFlow(flow2json))
print (switch.putFlow(flow3json))
print (switch.putFlow(flow4json))
print (switch.putFlow(flow5json))
print (switch.putFlow(flow6json))
print (switch.putFlow(flow7json))
print (switch.putFlow(flow8json))
print (switch.putFlow(flow9json))
print (switch.putFlow(flow10json))

host1.setHostId('00:00:00:00:01:01')
host1.setSwitchId(switch.getSwitchIds(data)[2])
host1.setNodeId(1)
host1.setVlan(1)
host1.buildPutHostJson()

host2.setHostId('00:00:00:00:01:02')
host2.setSwitchId(switch.getSwitchIds(data)[2])
host2.setNodeId(2)
host2.setVlan(1)
host2.buildPutHostJson()

host3.setHostId('00:00:00:00:01:03')
host3.setSwitchId(switch.getSwitchIds(data)[0])
host3.setNodeId(1)
host3.setVlan(1)
host3.buildPutHostJson()

host4.setHostId('00:00:00:00:01:04')
host4.setSwitchId(switch.getSwitchIds(data)[0])
host4.setNodeId(2)
host4.setVlan(2)
host4.buildPutHostJson()

host5.setHostId('00:00:00:00:01:05')
host5.setSwitchId(switch.getSwitchIds(data)[1])
host5.setNodeId(1)
host5.setVlan(2)
host5.buildPutHostJson()

host6.setHostId('00:00:00:00:01:06')
host6.setSwitchId(switch.getSwitchIds(data)[1])
host6.setNodeId(2)
host6.setVlan(2)
host6.buildPutHostJson()

print (switch.putHost(host1))
print (switch.putHost(host2))
print (switch.putHost(host3))
print (switch.putHost(host4))
print (switch.putHost(host5))
print (switch.putHost(host6))

topo1.setSrcNode(switch.getSwitchIds(data)[2])
topo1.setDstNode(switch.getSwitchIds(data)[0])
topo1.buildPutTopoJson()

topo2.setSrcNode(switch.getSwitchIds(data)[1])
topo2.setDstNode(switch.getSwitchIds(data)[0])
topo2.buildPutTopoJson()


print (switch.putTopo(topo1))
print (switch.putTopo(topo2))
