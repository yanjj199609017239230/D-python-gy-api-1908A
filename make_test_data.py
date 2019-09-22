#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/11'
import json
import os

import  yaml

from config.conf import FILE_PATH

POST = 1
GET = 0

mode_name = "charge"
test_case = "扣款异常流1金额为空"
method = POST
url = "/acc/charge" #接口地址
data = None
params = None
status_code = 200
headers = {}
expect = "2000"
json_data = '''{
  "accountName": "stdg2623",
  "changeMoney": 25
}''' #注意数据格式为字典或者为json串


if(isinstance(json_data,str)):
    json_data = json.loads(json_data)

d = [{
    "test_case":test_case,
    "method":method,
    "url":url,
    "data":data,
    "params":params,
    "json":json_data,
    "status_code":status_code,
    "expect":expect,
    "headers":headers

}]
with open(os.path.join(FILE_PATH,"test_{}.yaml".format(mode_name)),'a',encoding='utf-8') as f:
    yaml.safe_dump(d,f,encoding='utf-8',default_flow_style=False,allow_unicode=True)
    f.write("\n")
