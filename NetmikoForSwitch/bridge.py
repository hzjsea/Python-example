## 端口汇聚

from  netmiko import ConnectHandler
def cycle_gen_bridge():
    # 循环输出命令列表
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

    h3c_switch = {
        'device_type' : 'hp_comware',
        'host':   '10.0.5.124',
        'username': 'root',
        'password': 'upyun123',
    }
    net_connect = ConnectHandler(**h3c_switch)
    result = net_connect.send_config_set(cycle_gen_bridge)
    net_connect.disconnect()

    return result