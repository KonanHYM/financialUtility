# -*- coding:utf-8 -*-
#Bloomberg Data Anaylisis

import numpy as np
import pandas as pd
import math
import json

#要处理的bloomberg文件路径
file_path = "../file/bloomberg.xlsx"

#文件中包含的表单列表
index_list = [
    "NDX INDEX",
    "DJI INDEX",
    "SX5E INDEX",
    "SPX INDEX",
]

#需要处理的字段
index_fields = [
    "BEst NI:2016C\n",
    "BEst NI:2017C\n",
    "BEst NI:2018C\n",
    "Market Cap:D-1\n",
]

#bloomberg数据处理器
def bloombergParser():
    for index_name in index_list:
        parser = pd.read_excel(file_path, sheetname=index_name)
        parser = dataClean(parser)
        print '--------'
        print index_name
        for field in parser.columns:
            if field in index_fields:
                print field
                print parser[field].mean()

#将数据表中为空的数据统计出来
def dataClean(parser):
    for field in index_fields:
        for index_num in parser[field].index:
            if parser[field][index_num] == u'--':
                parser.drop(index_num, axis = 0)
    return parser

if __name__ == '__main__':
    bloombergParser()
