#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/12'
from tools import request_tool
from tools import assert_tool
from tools import random_tool
from tools import mysql_tool
from tools import excel_tool
from tools import log_tool
from tools import os_tool
from tools import shell_tool
import pytest
import allure
# 项目根目录建config包，里面建conf.py文件，用于配置
from config import conf





def request_tamp(d):
    status_code = d.pop("status_code")
    expect = d.pop("expect")
    method = d.pop("method")
    resp = None
    d["url"] = conf.GY_API_URL + d["url"]
    if(method==1):
        resp = request_tool.post_request(**d)
    else:
        resp = request_tool.get_request(**d)
    body = resp.json()
    # 判断响应码
    allure.attach("预期结果：{}，实际结果：{}".format(status_code, resp.status_code), "响应状态码断言", allure.attachment_type.TEXT)
    assert_tool.assert_equal(resp.status_code, status_code)
    # 自定义断言
    allure.attach("预期结果：{}，实际结果：{}".format(expect, resp.text), "响应正文断言", allure.attachment_type.TEXT)
    assert_tool.assert_in(resp.text, expect)