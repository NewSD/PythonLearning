#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: first-test.py
@time: 2019/9/25 22:11
@tools: PyCharm
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


def buildConnectionString(params):
    """Build a connection string from a dictionary of parameters.

    Returns string."""
    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])


if __name__ == "__main__":
    myParams = {"server": "mpilgrim",
                "database": "master",
                "uid": "sa",
                "pwd": "secret"
                }
    print(buildConnectionString(myParams))
