#!/usr/bin/python2
# coding=utf-8
# @Date: 7/23/18
# @Author: HZH
"""

"""

class User:
    def __init__(self, email):
        self.email = email

    def get_id(self):
        return self.email

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True