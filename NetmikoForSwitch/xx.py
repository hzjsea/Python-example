from netmiko import Netmiko
from netmiko import ConnectHandler


hp_device = {
    'device_type': 'hp_comware',
    'host':   '10.0.5.124',
    'username': 'root',
    'password': 'upyun123',
}

# 连接设备
net_connect = ConnectHandler(**hp_device)
net_connect.enable()


class config_command_device:
    def __init__(self):
        super().__init__()

    # 直接输入配置
    def show_currenConfiguration(self, command, *args, **kwargs):
        if args is not None:
            config_command1 = [
                'public-key peer pub',
                    'public-key-code begin',
                        '30820122300D06092A864886F70D01010105000382010F003082010A0282010100D37D67EC \
                        5A9466CD38895097E74386EBBEFA9EC59236DF5E96D7514B2903C21F09C6D47D74792B5E3D \
                        C1F99DB4D43614AE3AD61DEFFAF35CED9B94DBD85DE174598C491FA043F8C700DA686BFFCA \
                        227E4E7417A251CD7590673B4C1A227962F65CBA6017329479484EF8FE48A8E2FED636C846 \
                        5765801A0D62C821906FF8E7188DA69D716FD392E8C0D4D0618E9020670FFA24CF083E2EF7 \
                        690EABCA43AA4341D798A72B6FFB5A0A1BEF0F4B14B6B66E5F7126582BD11A11F4220EA3FF \
                        C1A5DF36E86E76A8EF6A97949158F094CBAD09725069A090CBA36D95CB6A9531A5AB8B3ED5 \
                        8D6C63C8138320F0F1ECD7B25203A1B79FC82635B0F53475BC428B3B741F0203010001',
                    'public-key-code end',
                'peer-public-key end',
            ]
            # config_command1 = [
            #     'vlan 1',
            #     'int vlan-interface 1',
            #     'display this'
            # ]
            net_connect.find_prompt()
            # output = net_connect.send_command_timing(config_command1,strip_command=False, normalize=False,strip_prompt=False)
            output = net_connect.send_config_set(config_command1)
            # output = net_connect.send_command("display cu")
            print(output)
        else:
            config_command1 = "display cu"
            net_connect.find_prompt()
            output = net_connect.send_command(config_command1)
            print(output)
            # return output

    # 输入file进行配置
    # def set_fileConfiguration(self,file_path,*args,**kwargs):
    #     net_connect.find_prompt()
    #     output = net_connect.send_config_from_file(file_path)
    #     print(output)

    # ##  配置
    # def set_fil


if __name__ == '__main__':
    ccd = config_command_device()
    ccd.show_currenConfiguration("display cu")
    # ccd.set_fileConfiguration('/Users/alpaca/PycharmProjects/NetmikoForSwitch/xx');
