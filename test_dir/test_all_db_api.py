#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_all_db_api.py    
@Contact :   746832476@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/11 上午12:20   luoqingfu   1.0         None
'''

# import lib
import pytest

from common.base import Base
from common.db_tool import read_api
from conftest import baseurl


class TestAllDbApi(Base):

    @pytest.mark.parametrize('dict', read_api())
    def test_all_api(self, dict):
        api_name = dict['api_name']
        url = dict['url']
        api_method = dict['api_method']
        request_data = dict['request_data']
        url = baseurl + url
        if api_method == 'post':
            res = self.http_request(api_method, url, request_data)
            assert res['code'] == 200
        elif api_method == 'get':
            res = self.http_request(api_method, url, request_data)
            assert res['code'] == 200


if __name__ == '__main__':
    TestAllDbApi().test_all_api()
