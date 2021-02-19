#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Contact :   746832476@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/2 3:17 下午   luoqingfu   1.0         None
'''

# import lib
import logging
import os

import pytest
import requests
import yaml

from common.base import Base
from conftest import baseurl
from test_def.login import Login

ProjectPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  # 获取当前项目路径上一级目录
yaml_path = ProjectPath + '/api'


# 读取文件
def yaml_data_with_file(file_name):
    with open(file_name + '.yaml', encoding='utf-8') as f:
        return yaml.safe_load(f)


# 读取yaml数据中的key值，这里的yaml文件名是data
def yaml_data():
    print(yaml_path)
    return yaml_data_with_file(yaml_path)


class TestAll(Login, Base):

    @pytest.mark.parametrize('dict', yaml_data())
    def test_all(self, dict):
        log = logging.getLogger('TestAll')
        # log.info('dict: '+str(dict))
        flag = dict['flag']
        caseName = dict['caseName']
        if flag == 0:
            pytest.skip('此条接口跳过验证{}'.format(caseName))

        url = baseurl + dict['url']
        method = dict['method']
        data = dict['request']

        if dict['method'] == 'post':
            log.info('开始测试{}'.format(caseName))
            res = self.http_request(method, url, data)
            assert res['code'] == 200
        else:
            log.info('开始测试{}'.format(caseName))
            res = self.http_request(method, url, data)
            assert res['code'] == 200


if __name__ == '__main__':
    TestAll().test_all()
