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

data = json.loads(html)

num = len(data["lineup"]["away"])
num2 = len(data["lineup"]["home"])

for i in range(0, num):
    if data["lineup"]["away"][i]["posOrder"] == "-1":
        pass
    else:
        print (data["gameInfo"]["dateTime"], end='')
        print(',', end='')
        print("인천 : ", end='')
        print(data["lineup"]["away"][i]["pName"], end='')               #플레이어 이름
        print(',', end='')
        print(data["lineup"]["away"][i]["pos"], end='')                 #포지션
        print(',', end='')
        print(data["lineup"]["away"][i]["posOrder"], end='')            #수비위치
        print(',', end='')
        if 'sTime' in data["lineup"]["away"][i]:
            if data["lineup"]["away"][i]["sType"] == "in":
                stime = 90 - int(data["lineup"]["away"][i]["sTime"])
                print(stime, end='')
                print(',', end='')                                            #출전시간
            else:
                print(data["lineup"]["away"][i]["sTime"], end='')
                print(',', end='')                                            #출전시간
        else:
            print("90", end='')
            print(',', end='')                                            #출전시간  
        print(data["lineup"]["away"][i]["goal"])  

print("=========================================")
'''
for j in range(0, num):
    print(data["lineup"]["home"][j]["pName"])    
'''