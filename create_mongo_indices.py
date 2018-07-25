#!/usr/bin/python2
# coding=utf-8
# @Date: 7/25/18
# @Author: HZH
"""

"""
import pymongo
client = pymongo.MongoClient()
c = client['waitercaller']
print c.users.create_index("email", unique=True)
print c.requests.create_index("table_id", unique=True)
