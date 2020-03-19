#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import math
import sys
import shutil
import re


path_nowfile = os.path.abspath(__file__)  # 当前脚本文件路径
path_files = os.path.join(os.path.dirname(
    path_nowfile), "tmpfiles")+os.path.sep  # 分隔文件存放点
path_sslog = os.path.join(os.path.dirname(
    path_nowfile), 'log', 'all.txt')  # 日志文件存放点


class cutfile:
    """
    func: 处理ss.log 分隔成多个文本
    """

    def __init__(self, nowfile, files, sslog):
        self.nowfile = path_nowfile
        self.files = path_files
        self.sslog = path_sslog

    # 获取日志行数
    def get_total_lines(self):
        # 如果不存在当前文件，则返回0行
        # 如果存在，则使用wc -l获取当前行数
        if not os.path.exists(self.sslog):
            return 0
        else:
            cmd = 'wc -l %s' % self.sslog
            # os.popen可以看一下
            return os.popen(cmd).read().split(" ")[3]

    # 根据文本行数切割
    def get_files(self):

        # 重置limit_cnt
        limit_cnt = 5000

        # 重置文件夹
        shutil.rmtree(self.files)
        os.mkdir(self.files)

        # 切割文件放入files中
        path_files_new = os.path.join(self.files, "newfile")
        command = "split -l%d  %s %s" % (limit_cnt, path_sslog, path_files_new)
        os.system(command)
        _list = os.listdir(path_files)
        return _list
# 处理分隔后的文本


class deal_files:

    def __init__(self):
        pass

    def deal_file_sigle(self, newfiles):
        num = 0
        minrrt_list = []
        dict_single = {}
        dict_list = []
        # 第一步 清除上下行数据，将内容整理成一个有规律的文本
        txt = os.popen("cat %s" % os.path.join(
            path_files, newfiles)).read().split()
        # 记录每一个列表中最后一个字符 minrrt的序号
        for fileds in txt:
            search_obj = re.match('minrtt:*.+', fileds)
            if search_obj == None:
                num += 1
            else:
                num += 1
                minrrt_list.append(num)
        minrrt_list.append(0)
        # print(len(minrrt_list))

#   ========> 过滤字段 添加内容 请看这里
        for i in range(len(minrrt_list)):
            # for i in range(2):
            dict_state = {}
            if i < len(minrrt_list)-1:
                # index,next_index
                for j in range(minrrt_list[i], minrrt_list[i+1]):
                    if txt[j] == "ESTAB" :
                        # 源ip
                        # ====> 源ip带端口
                        SAddress = txt[j+3].replace("::ffff:", "")
                        if SAddress.split(":")[0] == "127.0.0.1":
                            # print(SAddress)
                            continue
                        else:
                            SAddress = SAddress

                        # ====> 源ip不带端口
                        # SAddress = txt[j+3].replace("::ffff:", "").split(":")
                        # if len(SAddress) > 2:
                            # SAddress.pop()
                            # SAddress = ':'.join(SAddress)
                        # else:
                            # SAddress = SAddress[0]
                        # 源 port
                        SPort = txt[j+3].replace("::ffff:", "").split(":")[-1]
                        


                        # 目的 ip
                        DAddress = txt[j+4].replace("::ffff:","").split(":")
                        if len(DAddress) > 2:
                            DAddress.pop()
                            DAddress.pop()
                            DAddress.pop()
                            DAddress = ':'.join(DAddress)
                        else:
                            DAddress = DAddress[0]
                        # 目的 port
                        DPort = txt[j+4].replace("::ffff:","").split(":")[-1]

                        # 拥塞算法
                        algorithm = txt[j+5]

                        #rtt
                        rtt = float(txt[j+8].split(":")[1].split("/")[0])

                        # cwnd
                        try:
                            cwnd = int(txt[j+13].split(":")[1])
                        except:
                            cwnd = 0
                        
                        dict_state.setdefault("line_state",txt[j])
                        dict_state.setdefault("Saddress",SAddress)
                        # dict_state.setdefault("Sport",SPort)
                        dict_state.setdefault("Daddress",DAddress)
                        # dict_state.setdefault("Dport",DPort)
                        dict_state.setdefault("type",algorithm)
                        dict_state.setdefault("rtt",rtt)
                        dict_state.setdefault("cwnd",cwnd)

                    # Retrans
                    search_obj = re.match("retrans:*.+",txt[j])
                    # print(search_obj)
                    if search_obj == None:
                        if "Retrans" not in dict_state:
                            dict_state["Retrans"] = 0
                        else:
                            pass
                    else:
                        Retrans = search_obj.group(0).split(":")[1].split("/")[0]
                        dict_state["Retrans"] = Retrans
                        # print(dict_state)
                    # send
                    if txt[j] != "send":
                        if "send" not in dict_state:
                            dict_state["send"] = 0
                        else:
                            pass
                        # print(dict_state)
                    else:
                        send_value = re.match("\d+.\d+",txt[j+1]).group()
                        try:
                            send_speed = re.search("[MK]bps",txt[j+1]).group()
                        except:
                            send_speed = "Mbps"
                        if send_speed == "Mbps":
                            send_value = send_value
                        elif send_speed == "Kbps":
                            send_value = round((float(send_value)/1000),2)
                        else:
                            send_value = send_value
                
                        dict_state["send"] = send_value    
                    dict_list.append(dict_state)
                
                # print(dict_state)
                # dict_single.setdefault(str(i), dict_state)
            else:
                pass
        # print(dict_list)
        return dict_list

    def deals(self):
        end_dict = {}
        ct = cutfile(nowfile=path_nowfile, files=path_files, sslog=path_sslog)
        file_lists = ct.get_files()

        # test file_lists:[3:] => 只循环一组
        for i in file_lists:
            dict_singles = self.deal_file_sigle(i)
            end_dict.setdefault(str(i),dict_singles)
        return end_dict


if __name__ == "__main__":
    ct = cutfile(nowfile=path_nowfile, files=path_files, sslog=path_sslog)

    df = deal_files()
    tt =  df.deals()
 