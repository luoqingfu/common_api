#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_01_login.py    
@Contact :   746832476@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/2/18 下午3:59   luoqingfu   1.0         None
'''

# import lib
import logging

import pytest
import requests

from conftest import phone, password
from test_def.login import Login

logging.basicConfig(level=logging.DEBUG)


class TestLogin(Login):
    def test_login_with_pwd(self):
        """测试使用密码登录"""
        assert 1 == 2


if __name__ == '__main__':
    TestLogin().test_login_with_pwd()
