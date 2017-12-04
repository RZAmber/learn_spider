#! /usr/bin/env python
# -*-coding:utf-8 -*-

"""
@author:Xiuzhu
@file:spide_jike.py
@time:2017/12/4 11:17
"""


# http://www.jikexueyuan.com/course/
# requests获取网页
# re.sub换页
# 正则表达式匹配内容


import re
import requests
import importlib,sys
importlib.reload(sys)

class spider:
    def __init__(self):
        print("开始读取内容...")

    def changePage(self,url,total_page):
        now_page = int(re.search("pageNum=(\d+)", url, re.S).group(1))
        page_group = []
        for i in range(now_page, total_page+1):
            link = re.sub('pageNum=\d+','pageNum=%s'%i, url, re.S)
            page_group.append(link)
        return page_group

    def getSource(self,url):
        html = requests.get(url)
        return html.text

    def getAllClass(self, source):
        classList = re.findall('(<li id=.*?</li>)', source, re.S)
        return classList

    def getInfo(self, eachClass):
        info = {}
        title = re.search('class="lessonimg" title="(.*?)" alt=', eachClass, re.S).group(1)
        info['title'] = re.sub('\n\t\t\t','',title)
        # info['title'] = re.search('class="lessonimg" title="(.*?)" alt=', eachClass, re.S).group(1)
        content = re.search('display: none;">(.*?)</p>', eachClass, re.S).group(1)
        info['content'] = re.sub('\n\t\t\t', '', content)
        # info['content'] = re.search('display: none;">(.*?)</p>', eachClass, re.S).group(1)
        timeAndLevel = re.findall('<em>(.*?)</em>', eachClass, re.S)
        info['classTime'] = timeAndLevel[0]
        info['classLevel'] = timeAndLevel[1]
        info['learnNum'] = re.search('"learn-number">(.*?)</em>', eachClass, re.S).group(1)
        return info

    def saveInfo(self, classinfo):
        f = open('info.txt','a+')
        for each in classinfo:
            f.write('title:' + each['title'] +'\n')
            f.write('content:' + each['content'] + '\n')
            f.write('classTime:' + each['classTime'] + '\n')
            f.write('classLevel:' + each['classLevel'] + '\n')
            f.write('learnNum:' + each['learnNum'] + '\n\n')
        f.close()


if __name__ == '__main__':
    classinfo = []
    url = 'http://www.jikexueyuan.com/course/?pageNum=1'
    jike = spider()
    all_links = jike.changePage(url,20)
    for link in all_links:
        print("正在处理页面：" + link)
        html = jike.getSource(link)
        eachClass = jike.getAllClass(html)
        for each in eachClass:
            info = jike.getInfo(each)
            print(info)
            classinfo.append(info)
    jike.saveInfo(classinfo)