from netmiko import Netmiko 
from netmiko import ConnectHandler ##  此 factory 函数根据设备类型选择正确的 Netmiko 类

## 定义一个由设备类型、 ip、用户名和密码组成的网络设备字典。
hp_device = {
    'device_type' : 'hp_comware',
    'host':   '10.0.5.124',
    'username': 'root',
    'password': 'upyun123',
}

# -------------------------------------
## 连接设备
net_connect = ConnectHandler(**hp_device) 
## 或者这样
# net_connect = ConnectHandler(
#     device_type = 'hp_comware',
#     host = '10.0.5.124',
#     username = 'root',
#     password = 'upyun123',
# )
# -------------------------------------

## 建立远程连接
# net_connect.find_prompt()
## 发送指令
# output = net_connect.send_command(“display ip int brief")


## --- 配置多条命令
## 配置一个完成的acl实例
config_command = [
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
netmiko.send_command(config_commadn)

