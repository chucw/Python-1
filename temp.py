#-*- coding: utf-8 -*
import re
import requests as rq
import json
import calendar
import pandas
import sys


url = "https://sports.news.naver.com/wfootball/schedule/index.nhn?category=seria&year=2019&month=08"
html = rq.get(url).text

#print (html)

#matched = re.search(r'dailyScheduleListMap":(.*?;)', html, re.S)

#matched = re.search(r'scheduleList:(.*)', html)
matched = re.search(r'monthlyScheduleDailyGroup":(.*)', html, re.S)

tt = matched.group(1)

c1 = tt.find("monthList")
#print(c1)

src = tt[:c1-2]

#print(src)



for i in range(1, 31):
#    print(i)
#    print(json.loads(src)[i])
    src1 = json.loads(src)[i]
#    print(src1['date'])
#    print(src1['scheduleList'])
    s_empty = str(src1['empty'])
#    s_empty = s_empty.strip()

    if s_empty != 'true':
#        print(src1['date'])
#        print(src1['scheduleList'])


        obj = src1['scheduleList']
        for j in range(0, len(obj)):
            if obj[j]['homeTeamName'] is None:
                pass
            else:
                print(src1['date'])
                print(obj[j]['homeTeamName'])
                print(obj[j]['awayTeamName'])
                print(obj[j]['homeTeamScore'])
                print(obj[j]['awayTeamScore'])



print('OK')