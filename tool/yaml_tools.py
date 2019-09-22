#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/12'
import yaml


def read_yaml(file_path):
    d = None
    with open(file_path,'rb') as f:
        cont = f.read()
        cont=cont.decode('utf8')
        d = yaml.safe_load(cont)
    return d
