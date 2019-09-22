#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/12'
import os

import allure
import pytest

from config.conf import FILE_PATH
from tool.get_data import get_datas
from tool.request_tamp import request_tamp

data = get_datas(os.path.join(os.path.dirname(__file__),"../../data/test_recharge.yaml"))



@pytest.mark.parametrize("d",data[1],ids=data[0])
@allure.epic("一级标题")
@allure.feature("二级标题")
@allure.story("三级标题")
def test_run1(d):
    request_tamp(d)



data = get_datas(os.path.join(os.path.dirname(__file__),"../../data/test_charge.yaml"))



@pytest.mark.parametrize("d",data[1],ids=data[0])
@allure.epic("一级标题")
@allure.feature("二级标题")
@allure.story("三级标题")
def test_run2(d):
    request_tamp(d)


