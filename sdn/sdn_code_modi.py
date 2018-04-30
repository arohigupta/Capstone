import ryufunc
from ryuswitch import RyuSwitch
import json

#Get DPID's of switches
ryufunc.API="http://10.0.0.6:8080"
DPID_list=ryufunc.get_switches()
print (DPID_list)


#Get all flows for DPIDs
for DPID in DPID_list:
    flowStat=ryufunc.get_flow_stats(DPID)
    print (flowStat)
    flows=ryufunc.get_flows(DPID)
    print (flows)

#switchS1
mac1="d2:57:56:c1:e6:03"
mac2="b6:d8:72:7f:c0:48"
mac3="b6:9b:d6:1f:53:c5"
payload={"dpid":1, "cookie":0, "table_id":0, "idle_timeout":0, 
         "hard_timeout":0,"priority":32768, "match":{"dl_dst":mac2, "in_port":1},"actions":[{"type":"OUTPUT","port":2}]
        }
payload1={"dpid":1, "cookie":0, "table_id":0, "idle_timeout":0,
         "hard_timeout":0,"priority":32768, "match":{"dl_dst":mac1, "in_port":2},"actions":[{"type":"OUTPUT","port":1}]
        }
payload2={"dpid":1, "cookie":0, "table_id":0, "idle_timeout":0,
         "hard_timeout":0,"priority":32768, "match":{"dl_dst":mac2, "in_port":4},"actions":[{"type":"OUTPUT","port":3}]
        }
payload3={"dpid":1, "cookie":0, "table_id":0, "idle_timeout":0,
         "hard_timeout":0,"priority":32768, "match":{"dl_dst":mac3, "in_port":3},"actions":[{"type":"OUTPUT","port":4}]
        }


ryufunc.add_flow(payload)
ryufunc.add_flow(payload1)
ryufunc.add_flow(payload2)
ryufunc.add_flow(payload3)
flows=ryufunc.get_flows(1)
print flows

#switch s2
payload={"dpid":2, "cookie":0, "table_id":0, "idle_timeout":0,
         "hard_timeout":0,"priority":32768, "match":{"dl_dst":mac2, "in_port":1},"actions":[{"type":"OUTPUT","port":2}]
        }
payload1={"dpid":2, "cookie":0, "table_id":0, "idle_timeout":0,
         "hard_timeout":0,"priority":32768, "match":{"dl_dst":mac1, "in_port":2},"actions":[{"type":"OUTPUT","port":1}]
        }

ryufunc.add_flow(payload)
ryufunc.add_flow(payload1)

#switch s4
payload={"dpid":4, "cookie":0, "table_id":0, "idle_timeout":0,
         "hard_timeout":0,"priority":32768, "match":{"dl_dst":mac2, "in_port":1},"actions":[{"type":"OUTPUT","port":2}]
        }
payload1={"dpid":4, "cookie":0, "table_id":0, "idle_timeout":0,
         "hard_timeout":0,"priority":32768, "match":{"dl_dst":mac3, "in_port":2},"actions":[{"type":"OUTPUT","port":1}]
        }
ryufunc.add_flow(payload)
ryufunc.add_flow(payload1)


flows=ryufunc.get_flows(2)
print (flows)

#switch s3
payload={"dpid":3, "cookie":0, "table_id":0, "idle_timeout":0,
         "hard_timeout":0,"priority":32768, "match":{"dl_dst":mac2, "in_port":1},"actions":[{"type":"OUTPUT","port":3}]
        }
payload1={"dpid":3, "cookie":0, "table_id":0, "idle_timeout":0,
         "hard_timeout":0,"priority":32768, "match":{"dl_dst":mac1, "in_port":3},"actions":[{"type":"OUTPUT","port":1}]
        }
payload2={"dpid":3, "cookie":0, "table_id":0, "idle_timeout":0,
         "hard_timeout":0,"priority":32768, "match":{"dl_dst":mac3, "in_port":3},"actions":[{"type":"OUTPUT","port":2}]
        }
payload3={"dpid":3, "cookie":0, "table_id":0, "idle_timeout":0,
         "hard_timeout":0,"priority":32768, "match":{"dl_dst":mac2, "in_port":2},"actions":[{"type":"OUTPUT","port":3}]
        }


ryufunc.add_flow(payload)
ryufunc.add_flow(payload1)
ryufunc.add_flow(payload2)
ryufunc.add_flow(payload3)

#ARP
payload={"dpid":1, "cookie":0, "table_id":0, "idle_timeout":0,
         "hard_timeout":0,"priority":32768, "match":{"dl_src":mac1, "dl_type":0x0806},"actions":[{"type":"OUTPUT","port":2}]
        }

payload1={"dpid":2, "cookie":0, "table_id":0, "idle_timeout":0,
         "hard_timeout":0,"priority":32768, "match":{"dl_src":mac1, "dl_type":0x0806},"actions":[{"type":"OUTPUT","port":2}]
        }

payload2={"dpid":3, "cookie":0, "table_id":0, "idle_timeout":0,
         "hard_timeout":0,"priority":32768, "match":{"dl_src":mac1, "dl_type":0x0806},"actions":[{"type":"OUTPUT","port":3}]
        }

payload3={"dpid":3, "cookie":0, "table_id":0, "idle_timeout":0,
         "hard_timeout":0,"priority":32768, "match":{"dl_src":mac2, "dl_type":0x0806},"actions":[{"type":"OUTPUT","port":1}]
        }

payload4={"dpid":2, "cookie":0, "table_id":0, "idle_timeout":0,
         "hard_timeout":0,"priority":32768, "match":{"dl_src":mac2, "dl_type":0x0806},"actions":[{"type":"OUTPUT","port":1}]
        }

payload5={"dpid":1, "cookie":0, "table_id":0, "idle_timeout":0,
         "hard_timeout":0,"priority":32768, "match":{"dl_src":mac2, "dl_type":0x0806},"actions":[{"type":"OUTPUT","port":1}]
        }

payload6={"dpid":1, "cookie":0, "table_id":0, "idle_timeout":0,
         "hard_timeout":0,"priority":32768, "match":{"dl_src":mac3, "dl_type":0x0806},"actions":[{"type":"OUTPUT","port":2}]
        }
payload7={"dpid":2, "cookie":0, "table_id":0, "idle_timeout":0,
         "hard_timeout":0,"priority":32768, "match":{"dl_src":mac3, "dl_type":0x0806},"actions":[{"type":"OUTPUT","port":2}]
        }
payload8={"dpid":3, "cookie":0, "table_id":0, "idle_timeout":0,
         "hard_timeout":0,"priority":32768, "match":{"dl_src":mac3, "dl_type":0x0806},"actions":[{"type":"OUTPUT","port":3}]
        }






ryufunc.add_flow(payload)
ryufunc.add_flow(payload1)
ryufunc.add_flow(payload2)
ryufunc.add_flow(payload3)
ryufunc.add_flow(payload4)
ryufunc.add_flow(payload5)
ryufunc.add_flow(payload6)
ryufunc.add_flow(payload7)
ryufunc.add_flow(payload8)

flows=ryufunc.get_flows(1)
print flows
flows=ryufunc.get_flows(2)
print flows
flows=ryufunc.get_flows(3)
print flows
flows=ryufunc.get_flows(4)
print flows
