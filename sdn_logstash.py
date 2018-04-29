import ryufunc
from ryuswitch import RyuSwitch
import socket
import time
import json
import simplejson

ryufunc.API="http://10.0.0.6:8080"
#Get port stat
x=str(1)+"/"+str(2)
dicta={}

Port2stat=ryufunc.get_port_stats(x)
x=Port2stat[u'1'][0][u'tx_packets']
y=Port2stat[u'1'][0][u'tx_bytes']
dicta['tx_packets']=x
dicta['tx_bytes']=y

y=json.dumps(dicta)
jsonObj=json.loads(str(y))
print jsonObj
portno=25835
addr="127.0.0.1"

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.sendto(str(y),(addr, portno))
serverSock.close()
