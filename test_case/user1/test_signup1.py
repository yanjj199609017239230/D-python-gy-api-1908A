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
@allure.epic("商城后台系统")
@allure.feature("用户模块")
@allure.story("注册接口")
@allure.title('phone字段异常流_为空1')
def test_zhu_ce8():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/signup'

    req = {
        "phone": "",
        "pwd": "aaaaaaaafffff344",
        "rePwd": "aaaaaaaafffff344",
        "userName": "reye79"
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




