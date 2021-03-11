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

def read_api():
    """根据用户id获取uid"""
    connection = pymysql.connect(db='common_api_db', user='root', password='12345678', host='127.0.0.1',
                                 port=3306, charset='utf8')
    cursor = connection.cursor(pymysql.cursors.DictCursor)  # 以字典的方式获取在数据库中的api
    cursor.execute('SELECT {},{},{},{},{} FROM api WHERE flag = 1 and status = 1'.format('api_name', 'url', 'api_method', 'request_data', 'project_id'))
    result = cursor.fetchall()
    connection.close()
    return result



if __name__ == '__main__':
    read_api()