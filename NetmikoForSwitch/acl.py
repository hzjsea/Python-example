from netmiko import Netmiko
# 获取设备句柄
from netmiko import ConnectHandler

def acl_config_commands():
    h3c_switch = {
        'device_type' : 'hp_comware',
        'host':   '10.0.5.124',
        'username': 'root',
        'password': 'upyun123',
    }

    acl_config_commands = [
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


    net_connect = ConnectHandler(**h3c_switch)
    result = net_connect.send_config_set(acl_config_commands)
    net_connect.disconnect()

    return result


