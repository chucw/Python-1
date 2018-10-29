#-*- coding: utf-8 -*
import re
import requests as rq
import json
import calendar
import pandas
import pymysql
import sys

url = "https://sports.news.naver.com/wfootball/schedule/index.nhn?category=europa&year=2018&month=10"
html = rq.get(url).text

# print (html)

#matched = re.search(r'dailyScheduleListMap":(.*?;)', html, re.S)
matched = re.search(r'monthlyScheduleModel:(.*)', html)

tt = matched.group(1)
tt = tt[:-1]

data = json.loads(tt)

aaa = data["dailyScheduleListMap"]

print(tt)