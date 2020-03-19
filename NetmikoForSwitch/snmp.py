# 获取设备句柄
from netmiko import ConnectHandler

def snmp_config_commadns():
    h3c_switch = {
        'device_type' : 'hp_comware',
        'host':   '10.0.5.124',
        'username': 'root',
        'password': 'upyun123',
    }

    snmp_config_commands = [
        'snmp',
        'snmp-agent local-engineid 800063A203',
        'snmp-agent community read hgE6ofdZ3b',
        'snmp-agent sys-info version v2c v3',
        'snmp-agent trap source LoopBack0',
        'snmp-agent trap log',
    ]


    net_connect = ConnectHandler(**h3c_switch)
    result = net_connect.send_config_set(snmp_config_commands)

    net_connect.disconnect()
    return result


