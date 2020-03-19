from netmiko import Netmiko
from netmiko import ConnectHandler

class ConfigStatic(object):
    def __init__(self,h3c_switch=None):
        self.h3c_switch = {
            'device_type' : 'hp_comware',
            'host':   '10.0.5.124',
            'username': 'root',
            'password': 'upyun123',
        }

    @property
    def get_config(self):
        return self.h3c_switch