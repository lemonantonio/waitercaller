#!/usr/bin/python2
# coding=utf-8
# @Date: 7/22/18
# @Author: HZH
"""

"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Under construction"

if __name__=="__main__":
    app.run(host="0.0.0.0")
    