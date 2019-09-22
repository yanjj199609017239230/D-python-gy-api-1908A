
# 接口自动化封装框架



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

d = {}
d['username'] = 'bv2gcfgg56'

@allure.title('注册')
def test_liu_cheng1():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/signup'

    req = {
            "phone": "18667111947",
            "pwd": "bgks12ws",
            "rePwd": "bgks12ws",
            "userName": d['username']
    }
    resp = request_tool.post_request(url, json=req)
    body = resp.json()
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    allure.attach("预期结果:{},实际结果:{}".format(200,resp.status_code),"响应状态码断言",allure.attachment_type.TEXT)
    assert_tool.assert_equal(resp.status_code,200)
    # 自定义断言
    assert_tool.assert_equal(body['code'], 2000)
    allure.attach("预期结果:{},实际结果:{}".format(2000, body['code']), "响应code", allure.attachment_type.TEXT)
    assert_tool.assert_equal(body['code'], 2000)


@allure.title('登录')
def test_liu_cheng2():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/login'

    req = {
            "pwd": "bgks12ws",
            "userName": d['username']
    }
    resp = request_tool.post_request(url, json=req)
    body = resp.json()
    d["token"] = body ["data"]["token"]
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    allure.attach("预期结果:{},实际结果:{}".format(200,resp.status_code),"响应状态码断言",allure.attachment_type.TEXT)
    assert_tool.assert_equal(resp.status_code,200)
    # 自定义断言
    assert_tool.assert_equal(body['code'], 2000)
    allure.attach("预期结果:{},实际结果:{}".format(2000, body['code']), "响应code", allure.attachment_type.TEXT)
    assert_tool.assert_equal(body['code'], 2000)

@allure.title('修改密码')
def test_liu_cheng3():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/user/changepwd'
    pwd = random_tool.random_pwd()
    req = {
        "newPwd": "bgks12wfg2",
        "oldPwd": "bgks12wfg2",
        "reNewPwd": "bgks12wfg2",
        "userName": d['username']
    }
    a = {"token":d["token"]}

    resp = request_tool.post_request(url, json=req, headers=a)
    body = resp.json()
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    allure.attach("预期结果:{},实际结果:{}".format(200,resp.status_code),"响应状态码断言",allure.attachment_type.TEXT)
    assert_tool.assert_equal(resp.status_code,200)
    # 自定义断言
    assert_tool.assert_equal(body['code'], 2000)
    allure.attach("预期结果:{},实际结果:{}".format(2000, body['code']), "响应code", allure.attachment_type.TEXT)
    assert_tool.assert_equal(body['code'], 2000)
