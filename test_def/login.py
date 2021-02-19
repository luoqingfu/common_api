#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   login.py
@Contact :   746832476@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/29 8:19 下午   luoqingfu   1.0         None
'''

# import lib
import logging

import requests

from common.base import Base
from conftest import baseurl, phone

logging.basicConfig(level=logging.DEBUG)


class Login(Base):
    def login_with_phone_password(self, phone, password):
        """
        使用账号密码登录
        :return:
        """
        log = logging.getLogger('login_with_phone_password')
        url = baseurl + '/users/loginWithPhoneAndPassword'
        data = {
            'areaCode': "+86",
            'password': password,
            'mobilePhoneNumber': phone
        }
        msg = self.http_request('post', url, data)
        log.info('返回的msg为{}'.format(msg))
        return msg['success']


if __name__ == '__main__':
    # Login().log(13226349780, 'verify_code', 12345)
    Login().login_with_phone_password(13226349780, 123456)
