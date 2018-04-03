# -*- coding:utf-8 -*-
#Bloomberg Data Anaylisis

import numpy as np
import pandas as pd
import math
import json

#要处理的bloomberg文件路径
file_path_1 = "../file/DevelopedMarket.xlsx"
file_path_2 = "../file/EmergingMarket.xlsx"

#文件中包含的表单列表
index_list_dict = {
    "index_list_1" : [
        #"NDX INDEX",
        "SPX INDEX",
        "DJI INDEX",
        "SX5E INDEX",
        "UKX INDEX",
        "CAC INDEX",
        "DAX INDEX",
        "NKY INDEX",
        "HSI INDEX",
        "KOSPI2 INDEX",
    ],
    "index_list_2" : [
        "IBOV INDEX",
        "IPSA INDEX",
        "COLCAP INDEX",
        "MEXBOL INDEX",
        "SPBLPGPT INDEX",
        "SENSEX INDEX",
        "JCI INDEX",
        "FBMKLCI INDEX",
        "PCOMP INDEX",
        "SET INDEX",
        "PX INDEX",
        "ASE INDEX",
        "WIG INDEX",
        "RTSI$ INDEX",
        "EGX30 INDEX",
        "TOP40 INDEX",
        "XU100 INDEX",
    ]
}

#需要处理的字段
index_fields = [
    "NI / Profit:2016C\n",
    "BEst NI:2017C\n",
    "BEst NI:2018C\n",
    "Market Cap:D-1\n",
]

#结果字段
result_fields = [
    "NI / Profit:2016C\n",
    "BEst NI:2017C\n",
    "BEst NI:2018C\n",
    "Market Cap:D-1\n",
    "remark",
]

#bloomberg数据处理器
def bloombergParser(file_path):
    result = pd.DataFrame(columns=result_fields, index=index_list_dict['index_list_1'])
    print result
    for index_name in index_list_dict['index_list_1']:
        parser = pd.read_excel(file_path, sheetname=index_name)
        final_parser_list = dataClean(parser)
        parser = final_parser_list[0]
        empty_num = final_parser_list[1]
        print '--------'
        print index_name
        print "剔除"+str(empty_num)+"家"
        result['remark'][index_name] = "剔除"+str(empty_num)+"家"
        for field in parser.columns:
            if field in index_fields:
                print field
                print parser[field].sum()
                result[field][index_name] = parser[field].sum() / 100000000
    # print result
    writer = pd.ExcelWriter('output.xlsx')
    result.to_excel(writer,'Sheet2')
    writer.save()


#将数据表中为空的数据统计出来
def dataClean(parser):
    empty_num = 0
    ini_num = parser.shape[0]
    for field in index_fields:
        for index_num in parser[field].index:
            if parser[field][index_num] == u'--':
                print index_num
                print parser[field][index_num]
                parser = parser.drop(index_num, axis = 0)
    print parser.shape[0]
    empty_num = ini_num - parser.shape[0]
    return [parser, empty_num]

if __name__ == '__main__':
    bloombergParser(file_path_1)
    # bloombergParser(file_path_2)
