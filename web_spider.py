#! /usr/bin/env python
# -*- coding utf-8 -*-

"""
@author:Xiuzhu
@file:web_spider.py
@time:2017/12/4 10:26
"""

import re
import requests

##网页获取源代码
html = requests.get("https://www.nowcoder.com/courses")

content = re.findall('<h3>(.*?)</h3>', html.text, re.S)
for each in content:
    print(each)
