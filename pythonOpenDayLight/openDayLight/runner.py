'''
Created on Nov 14, 2013

@author: mikeoutland
'''
import json
import requests
from pythonOpenDayLight.openDayLight import odlSwitch

user = 'admin'
password = 'admin'
auth = (user, password)
flow = 'http://127.0.0.1:8080/controller/nb/v2/statistics/default/flow'
resp = requests.get(flow, auth=auth)
data = json.loads(resp.text)
switch = odlSwitch.odlSwitch('http://127.0.0.1:8080/controller/nb/v2/')
print (data)
print (switch.getSwitchIds(data))
print (switch.putFlow(switch.getNodeTypes(data)[0], switch.getSwitchIds(data)[0], 'flow0', '10.0.0.1', 1, 2))
print (switch.putFlow(switch.getNodeTypes(data)[0], switch.getSwitchIds(data)[0], 'flow1', '10.0.0.2', 2, 1))
print (switch.removeFlow(switch.getNodeTypes(data)[0], switch.getSwitchIds(data)[0], 'flow0'))
print (switch.removeFlow(switch.getNodeTypes(data)[0], switch.getSwitchIds(data)[0], 'flow1'))