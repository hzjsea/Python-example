from netmiko import Netmiko
from netmiko import ConnectHandler
from static_files import ConfigStatic

class base_switch(object):
    def __init__(self,switch_type=None,h3c_switch=None,acl_config_commands=None):
        cs = ConfigStatic()
        if h3c_switch is None:
            self.h3c_switch = cs.get_config
        else:
            self.h3c_switch = h3c_switch
        self.acl_config_commands = acl_config_commands

    """
        设置用户信息
    """
    def set_user_info(self,commands=None,root_user="root",service_type="ssh"):
        h3c_switch = self.h3c_switch
        commands = [
            "local-user xxx class manage",
            "password simple upyun123", 
            "service-type ssh",
            "authorization-attribute user-role level-3",
            "authorization-attribute user-role network-admin",
            "authorization-attribute user-role network-operator",
            "quit",
            "user-interface vty 0 4",
            "authentication-mode scheme",       
            "user-role network-admin",
            "protocol inbound all",
        ]
        
        net_connect = ConnectHandler(**h3c_switch)
        result = net_connect.send_config_set(commands)
        net_connect.disconnect() 
        return result
    
    """
        同步机器时间
    """
    def update_machine_time(self):
        h3c_switch = self.h3c_switch
        commands = [
            "interface Vlan-interface1",
            "ntp-service unicast-server 218.189.210.4 source Vlan-interface 1",
            "ntp-service unicast-server 137.189.4.10 source Vlan-interface 1",
            "clock timezone beijing add 8",
        ]
        net_connect = ConnectHandler(**h3c_switch)
        result = net_connect.send_config_set(commands)
        net_connect.disconnect() 
        return result

    """
        路由追踪 routingTrack
    """
    def routingTrack(self):
        h3c_switch = self.h3c_switch
        commands = [
            "ip ttl-expires enable",
            "ip unreachable enable",
            "ipv6 unreachable enable"
        ]

    """
        判断机器类型 determineType
        默认为H3C5130
    """
    def determineType(self):
        if self.switch_type is None:
            self.swicth_type = "H3C5130"
        elif  isinstance(self.swicth_type is 'str'):
            msg['state'] = 'run'
            if self.swicth_type == "H3C5130" or self.swicth_type == "H3C5120" or self.swicth_type == "H3C5820" or self.swicth_type == "H3C6800":
                return self.swicth_type
    
    """
        配置二层环路路由检测 secondLoopRouting
    """
    def secondLoopRouting(self):
        if self.swicth_type == "H3C5130" or self.swicth_type == "H3C5820" or self.swicth_type == "H3C6800":
            command = [
                "loopback-detection global enable vlan all",
                "shutdown-interval 120 ",
                "loopback-detection interval-time 5",
                "loopback-detection action shutdown",
                "loopback-detection enable vlan all",
            ]
        elif self.swicth_type == "H3C5120":
            command = [
                "loopback-detection multi-port-mode",
                "loopback-detection enable",
                "shutdown-interval 120 ",
                "loopback-detection interval-time 5",
                "loopback-detection action shutdown",
                "loopback-detection enable vlan all",
            ]

    """
        acl过滤
    """     
    def filterAcl(self):
        command = [
            "acl number 2000 ",
            "description Login IP Control",
            "rule 1 permit source 192.168.0.0 0.0.255.255",
            "rule 5 permit source 115.238.93.82 0",
            "rule 10 permit source 115.231.100.64 0.0.0.63",
            "rule 15 permit source 121.52.226.192 0.0.0.63",
            "rule 20 permit source 115.238.54.160 0.0.0.15",
            "rule 25 permit source 124.160.114.192 0.0.0.15",
            "rule 30 permit source 106.186.117.158 0.0.0.255",
            "rule 35 permit source 157.119.232.0  0.0.0.31",
            "rule 40 permit source 218.205.64.19 0.0.0.31",
            "rule 45 permit source 112.17.251.0 0.0.0.31",
            "rule 50 permit source 121.52.250.193 0.0.0.31",
            "rule 55 permit source 183.131.0.65 0.0.0.31",
            "rule 60 permit source 43.230.89.160 0.0.0.31",
            "rule 65 permit source 111.1.32.0 0.0.0.127",
            "rule 70 permit source 115.231.97.0 0.0.0.31",
            "rule 1000 deny source any",
        ]


    """
        设置汇聚口
        port有几种类型，根据交换机的类型来判断port的类型
    """
    def cycle_gen_bridge(self,swicth_type):
        cycle_gen_bridge = []
        for i in range(1,15):
            line1 = "interface bridge-aggregation %s"%i
            line2 = "interface GigabitEthernet1/0/%s"%int(i*2-1)
            line3 = "port link-aggregation group %s"%i
            line4 = "interface GigabitEthernet1/0/%s"%int(i*2)
            line5 = "port link-aggregation group %s"%i
            cycle_gen_bridge.append(line1)
            cycle_gen_bridge.append(line2)
            cycle_gen_bridge.append(line3)
            cycle_gen_bridge.append(line4)
            cycle_gen_bridge.append(line5)

    
    """
        设置snmp
    """
    def setSnmp(self):
        command = [
            'snmp',
            'snmp-agent local-engineid 800063A203',
            'snmp-agent community read hgE6ofdZ3b',
            'snmp-agent sys-info version v2c v3',
            'snmp-agent trap source LoopBack0',
            'snmp-agent trap log',
        ]


        
if __name__ == '__main__':
    bs = base_switch
    bs.set_user_info()

    

