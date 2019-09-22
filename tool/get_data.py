#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/12'
import os

from tool.yaml_tools import read_yaml

def get_datas(dir_path):
    datas = []
    ids = []
    if(os.path.isdir(dir_path)):
        dirs = os.listdir(dir_path)
        data_dir = os.path.abspath(dir_path)
        for d in dirs:
            if not d.endswith(".yaml"):
                continue
            file_path = os.path.join(data_dir,d)
            yaml_datas = read_yaml(file_path)
            for data in yaml_datas:
                ids.append(data.pop("test_case"))
                datas.append(data)
    else:
        if not dir_path.endswith(".yaml"):
            print("请输入一个yaml文件")
            return None,None
        yaml_datas = read_yaml(dir_path)
        for data in yaml_datas:
            ids.append(data.pop("test_case"))
            datas.append(data)
    return ids,datas



