#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   base.py
@Contact :   746832476@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/29 7:37 下午   luoqingfu   1.0         None
'''

# import lib

import requests


class Base():

    def http_request(self, method, url, data):
        '''
        简单封装一下get和post请求
        :param method:
        :param url:
        :param data:
        :return: 返回的json
        '''
        if method == 'get':
            res = requests.get(url, data)
        else:
            res = requests.post(url, data)

        msg = res.json()
        return msg

    # GET请求
    def request_get(self, url, data):
        self.http_request('get', url, data)

    # POST请求
    def request_post(self, url, data):
        self.http_request('post', url, data)
