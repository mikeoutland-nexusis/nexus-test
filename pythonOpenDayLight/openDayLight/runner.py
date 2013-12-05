'''
Created on Nov 14, 2013

@author: mikeoutland
'''

#In mininet i'm using the following config:
#    mn --topo single,3 --mac --switch ovsk --controller=remote,ip=10.0.2.2,port=6633
#    The current runner will setup a simple flow between h1 and h2 

from pythonOpenDayLight.openDayLight import odlSwitch, odlJson

switch = odlSwitch.odlSwitch('http://127.0.0.1:8080/controller/nb/v2/')
data = switch.getFlowStatJson()
host1json = odlJson.odlJson()
host2json = odlJson.odlJson()
host1json.setInPort(1)
host1json.setOutPort(2)
host2json.setInPort(2)
host2json.setOutPort(1)
host1json.setName('h1toh2')
host2json.setName('h2toh1')
host1json.setSwitchId(switch.getSwitchIds(data)[0])
host2json.setSwitchId(switch.getSwitchIds(data)[0])
host1json.buildPutFlowJson()
host2json.buildPutFlowJson()
print (data)
print (switch.getSwitchIds(data))
print (switch.putFlow(host1json))
print (switch.putFlow(host2json))


#print (switch.removeFlow(switch.getNodeTypes(data)[0], switch.getSwitchIds(data)[0], 'flow0'))
#print (switch.removeFlow(switch.getNodeTypes(data)[0], switch.getSwitchIds(data)[0], 'flow1'))