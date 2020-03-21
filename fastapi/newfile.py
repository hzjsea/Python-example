#!/usr/bin/env python3
# encoding: utf-8
'''
@author: hzj
@file: newfile.py
@time: 2020/3/17 4:26 下午
'''

# one capitalize() 将首字符转换成大写，首字母是符号的时候则不会转换
string="hzj"
print(string.capitalize())
string="+ hzj"
print(string.capitalize())


# center
string="hzj"


# 类型检测
from typing import Optional,List
def func(res: bool) -> List[str,str]:
    if res:
        print(res)
    else:
        print(False)

if __name__ == '__main__':
    func(False)

    