#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   db_tool.py
@Contact :   746832476@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/2/18 下午3:47   luoqingfu   1.0         None
'''

# import lib
import pymysql

class Db():
    def read_uid(self, erban_no):
        """根据用户id获取uid"""
        connection = pymysql.connect(db='xxxx', user='root', password='xxxxx', host='xxxxx',
                                     port=3306, charset='utf8')
        cursor = connection.cursor()
        cursor.execute('SELECT uid FROM users WHERE user_id = {}'.format(erban_no))
        result = cursor.fetchone()
        connection.close()
        return result[0] #result 返回的为元组，取第一个值