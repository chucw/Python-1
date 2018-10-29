#-*- coding: utf-8 -*
import re
import requests as rq
import pandas
import json
import pymysql
import sys


#url = "https://sports.news.naver.com/gameCenter/textRelayFootball.nhn?category=kleague&gameId=201810061718188"
url = "https://sportsdata.pstatic.net/ndata//kleague/2018/10/201810061718188.json"
html = rq.get(url).text

matched = re.search(r'"goalInfo":(.*)', html)

tt = matched.group(1)
tt = tt[:-1]

data = json.loads(tt)


print (data)