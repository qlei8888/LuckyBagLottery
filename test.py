#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Create: 2024/9/16 12:52
# @Author: liuzejin
"""
import uiautomator2

d = uiautomator2.connect("192.168.31.153:5556")
d(text="我").click()
print(d.info)

