# -*- coding utf-8 -*-

"""
@author:Amber
@file:spider.py
@time:2017/11/2913:56
"""

import re
import requests
##手动获取网页源代码进行爬虫
url = "http://www.jikexueyuan.com/"

#读取源代码
f = open('source.txt','r', encoding = 'UTF-8')
html = f.read()
f.close()

pic_url = re.findall('img src="(.*?)" class="lessonimg', html, re.S)
i = 0
for each in pic_url:
    print("downloading:" +each)
    pic = requests.get(each)
    fp = open("pic\\" +str(i) +".jpg",'wb')
    fp.write(pic.content)
    fp.close()
    i+=1