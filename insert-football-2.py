#-*- coding: utf-8 -*
import re
import requests as rq
import json
import calendar
import pandas
import pymysql
import sys

url_2 = "http://sports.news.naver.com/gameCenter/textRelayFootball.nhn?category=kleague&gameId=201810061718188"
html_2 = rq.get(url_2).text

# print (html)

#matched = re.search(r'dailyScheduleListMap":(.*?;)', html, re.S)
matched_2 = re.search(r'relayDataUrl:(.*)', html_2)

tt_2 = matched_2.group(1)
#tt_2 = tt_2[:-1]
print(tt_2)

#data = json.loads(tt_2)


##aaa = data['relayDataUrl']

#print(aaa)