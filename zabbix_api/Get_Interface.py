from __future__ import division
from zabbix_info import auth_token,header,url,interface_url,cdn_host,cdn_host_test
import requests
import json
import time

class _getdata():
    def __init__(self, url, auth_token, header, *args, **kwargs):
        self.url = url
        self.auth_token = auth_token
        self.header = header

    # zabbix host主机请求方法
    # return host_name host_id
    def get_host(self, cdn_host):
        post_data = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "filter": {
                    "name": cdn_host
                },
                "output": [
                    "hostid",
                ],
            },
            "id": 1,
            "auth": self.auth_token
        }

        ret = requests.post(self.url, data=json.dumps(post_data), headers=self.header)
        # print(ret)
        return ret




    # zabbix items 监控项请求方法
    def get_items(self, _hostids):
        post_data = {
            "jsonrpc": "2.0",
            "method": "item.get",
            "params": {
                "hostids": _hostids,
                "output": [
                    "itemids",
                    'key_'
                ]
            },
            "auth": self.auth_token,
            "id": 1
        }
        ret = requests.post(self.url, data=json.dumps(post_data), headers=self.header)
        return ret

    # zabbix  history 历史数据请求方法
    # return
    def get_history(self, _itemids):
        post_data = {
            "jsonrpc": "2.0",
            "method": "history.get",
            "params": {
                "output": "extend",
                "history": 3,
                "itemids": _itemids,
                "limit": 10,
                'sortfield': 'clock',
                'sortorder': 'DESC',
                'time_from': 1565577941,
                'time_till': 1565578241,
            },
            "id": 1,
            "auth": auth_token
        }
        ret = requests.post(url, data=json.dumps(post_data), headers=header)
        return json.loads(ret.text)




    def get_interface(self,host_name):
        result = requests.get(interface_url%(host_name)).json()
        return result


# 根据API获取监控项信息
def GetItem():
    getdata = _getdata(url, auth_token, header)
    result = getdata.get_host(cdn_host_test).json()['result'][0]['hostid']  # 获取hostid
    print(result)
    interface_type = getdata.get_interface("MIX-JS-CZX-S01")  # 获取交换机进出接口状态
    print(interface_type)
    # 获取当前交换机状态
    # 若在线 继续获取接口运行状态
    # 获取正在运行的接口的监控项ID
    status = interface_type['status']
    if status == 'online':
        switch_uplinks = interface_type['switch_uplink']
        for switch_uplink in switch_uplinks:
            if switch_uplink['status'] == True:
                return switch_uplink
    else:
        pass


if __name__ == '__main__':
    getdata = _getdata(url, auth_token, header)
    # _in = getdata.get_history("598852")['result']
    # _in_clock = getdata.get_history("598852")['result'][0]['clock']
    # for i in _in:
    #     _in_value = int(i['value'])
    #     _in_clock = time.gmtime(i['clock'])
    #     print(_in_value,_in_clock)

    res = getdata.get_host(cdn_host="POP-ZJ-XIH-S01")
    print(res)