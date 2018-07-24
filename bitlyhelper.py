#!/usr/bin/python2
# coding=utf-8
# @Date: 7/24/18
# @Author: HZH
"""

"""
import urllib2
import json

TOKEN = "a22484370bef5f3789c1e1eebb6dc4ad465d2a4c"
ROOT_URL = "https://api-ssl.bitly.com"
SHORTEN = "/v3/shorten?access_token={}&longUrl={}"

class BitlyHelper:
    def shorten_url(self, longurl):
        try:
            url = ROOT_URL + SHORTEN.format(TOKEN, longurl)
            response = urllib2.urlopen(url).read()
            jr = json.loads(response)
            res = jr['data']['url']
            if not res.startswith("https://"):
                res = res.replace("http://", "https://")
            return res
        except Exception as e:
            print e

b = BitlyHelper()
print b.shorten_url("http://119.23.254.170:5000/request/123")