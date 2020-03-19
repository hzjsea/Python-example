#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import json
import deal_file as ssfile
import time
from datetime import datetime
import math
import  socket

df = ssfile.deal_files()
end_dict = df.deals()

# 整理每个文件中的内容，将重叠的部分重合计算
# 先分个处理，后几个文件一起处理
class format_json:
    def __init__(self):
        self.same_sip_lists  = []

    def format_single_file(self,files):

        # 将不同Saddress的dict 先存放到list_tmp中再存放到以当前Saddress为key的字典中
        # 如果相同则存到同key字典中的list_tmp列表中
        same_sip_list = []
        same_sip_dict = []
        for td in files:
            list_tmp = []
            list_tmp2 = []
            list_dict = {}
            try:
                ip = td['Saddress']
            except:
                continue

            if ip not in same_sip_list:
                list_tmp.append(td)
                list_dict.setdefault(ip,list_tmp)
                same_sip_list.append(ip)
                same_sip_dict.append(list_dict)
            else:
                for i in same_sip_dict:
                    if ip in i.keys():
                        list_tmp2 = i[ip]
                        list_tmp2.append(td)
                        i[ip] = list_tmp2
                    else:
                        pass
                pass
        self.same_sip_lists = same_sip_list
        return same_sip_dict

    def get_avge(self,same_sip_dict):
        # print(len(same_sip_dict))
        lis = []
        for tmp_dict in same_sip_dict:
            rtt = 0
            cwnd = 0
            Retrans = 0
            send = 0
            dic = {}
            tmp_list = list(tmp_dict.values())[0]
            # print(tmp_list)
            # print(len(tmp_list))
            for i in range(len(tmp_list)):
                rtt = tmp_list[i]['rtt'] + rtt
                cwnd = tmp_list[i]['cwnd'] + cwnd
                # print(cwnd)
                Retrans = float(tmp_list[i]['Retrans']) + Retrans
                send = float(tmp_list[i]['send']) + send
            # print(tmp_list[i]['Retrans'])
            # print(len(tmp_list))
            rtt = round(float(rtt/len(tmp_list)),2)
            cwnd = round(float(cwnd/len(tmp_list)),2)
            Retrans = math.ceil(float(Retrans/len(tmp_list)))
            # if Retrans == 0:
            #     pass
            # else:
            #     print(Retrans)
            #     pass
            send = round(float(send/len(tmp_list)),2)
            # print(Retrans,send)
            timestamp =  datetime.now().strftime("%d/%b/%Y:%X +0800")
            total = len(tmp_list)
            hostname =  socket.gethostname()
            #全变成字符串
            # rtt = str(rtt)
            # cwnd = str(cwnd)
            # Retrans = str(Retrans)
            # send = str(send)

            # print(rtt)
            dic.setdefault("Daddress",tmp_list[0]['Daddress'])
            dic.setdefault("Saddress",tmp_list[0]['Saddress'].split(":")[0])
            dic.setdefault("SPort",tmp_list[0]['Saddress'].split(":")[-1])
            # print(tmp_list[0])
            dic.setdefault("rtt",rtt)
            dic.setdefault("cwnd",cwnd)
            dic.setdefault("Retrans",Retrans)
            dic.setdefault("send",send)
            dic.setdefault("total",total)
            # print(len(tmp_list))
            dic.setdefault("line_state",tmp_list[0]['line_state'])
            dic.setdefault("type",tmp_list[0]['type'])
            dic.setdefault("node_type","network-attack")
            dic.setdefault("timestamp",timestamp)
            dic.setdefault("hostname",hostname)
            lis.append(dic)
            # print(Retrans)
        return lis



    def get_dict(self):
        newfiles =  os.listdir(os.path.join(os.path.dirname (os.path.abspath(__file__)),"tmpfiles/"))
        list_iterator = []
        for i in newfiles:
            list_iterator = list_iterator + end_dict[i]
        # print(i)
        same_sip_dict = self.format_single_file(list_iterator)
        lis = self.get_avge(same_sip_dict)
        return lis

    def update_json(self):
        _str = ""
        lis = self.get_dict()
        for i in lis:
            _str_tmp = "\n"+json.dumps(i)
            _str = _str+_str_tmp
        print("'"+_str[1:]+"'")
if __name__ == "__main__":
    fj = format_json()
    # fj.get_dict()
    fj.update_json()
