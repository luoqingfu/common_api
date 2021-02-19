#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   rds_tool.py    
@Contact :   746832476@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/2/18 下午3:48   luoqingfu   1.0         None
'''

# import lib
# import lib
import redis
r = redis.StrictRedis(host='*****', port=0000, db=0, password=00000000, decode_responses=True)  #加上decode参数避免出现b''


class Rds():

    def read_ticket(self, key, uid, value):
        """读取对应uid的ticket"""
        if r.hget(key, uid) == None:
            #如果指定的key没有值，则设为指定的value
           key_value = r.hset(key, uid, value)
        else:
            key_value = r.hget(key, uid)
        return key_value

