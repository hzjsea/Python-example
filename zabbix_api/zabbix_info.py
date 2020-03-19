ZABBIX_MONITOR_ITEM = {
    'B': {
        'out': 'ifHCOutOctets[Bridge-Aggregation%s]',
        'in': 'ifHCInOctets[Bridge-Aggregation%s]'
    },
    'G': {
        'out': 'ifHCOutOctets[GigabitEthernet%s]',
        'in': 'ifHCInOctets[GigabitEthernet%s]'
    },
    'F': {
        'out': 'ifHCOutOctets[FortyGigE%s]',
        'in': 'ifHCInOctets[FortyGigE%s]'
    },
    'T': {
        'out': 'ifHCOutOctets[Ten-GigabitEthernet%s]',
        'in': 'ifHCInOctets[Ten-GigabitEthernet%s]'
    },
    'R': {
        'out': 'ifHCOutOctets[Route-Aggregation%s]',
        'in': 'ifHCInOctets[Route-Aggregation%s]'
    }
}



## zabbix api url地址
url = "http://zabbix.s.upyun.com/zabbix/api_jsonrpc.php"
## zabbix api 用户验证token
auth_token ="6e70d86858c0fd80f9a3bb094335a358"
## upyun zabbix 请求参数apikey值
apikey = "yBd5zoewTsYrGKKMPoNsjcTyyVevrheP"

## zabbix 请求头部
header = {'Content-Type': 'application/json-rpc','apikey':apikey}



cdn_host =[
    "POP-ZJ-XIH-S01",
    "POP-ZJ-HGH-KC1",
    "CNE-SAD-A21-CR1",
    "NGN-ZJ-SAD-S01",
]


cdn_host_test=[
    # "POP-ZJ-HGH-S01",
    "POP-BJ-PEK-S01",
    "POP-SH-SHA-S01",
]


SwitchInterface_test=[
    'Te1/0/24',
    'Te1/0/22'
]

# 流量进出接口请求地址
interface_url = "http://zbx-gather.test.s.upyun.com/zabbix/switch/%s.json"