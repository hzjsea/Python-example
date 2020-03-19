# 端口汇聚

from  netmiko import ConnectHandler


def getstatus(host):
    h3c_switch = {
        'device_type' : 'hp_comware',
        'host':   host,
        'username': 'root',
        'password': 'upyun123',
    }

    status_config_commands = [
        "dis int brief",
    ]

    net_connect = ConnectHandler(**h3c_switch)
    result = net_connect.send_config_set(status_config_commands)
    return result
    net_connect.disconnect()

if __name__ == '__main__':
    xx = getstatus("10.0.5.124")
    print(xx)