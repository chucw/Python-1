#-*- coding: utf-8 -*
import re
import requests as rq
import json
import calendar
import pandas
import pymysql
import sys


url = "https://sports.news.naver.com/wfootball/schedule/index.nhn?category=primera&year=2019&month=09"
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


conn = pymysql.connect(host='localhost', port=3306,  db='betman', user='root', password='syjm1998')
curs = conn.cursor()

for i in range(1, 30):
#    print(i)
#    print(json.loads(src)[i])
    src1 = json.loads(src)[i]
#    print(src1['date'])
#    print(src1['scheduleList'])
    s_empty = str(src1['empty'])
#    s_empty = s_empty.strip()

    if s_empty == 'False':
#        print(src1['date'])
#        print(src1['scheduleList'])

        obj = src1['scheduleList']
        for j in range(0, len(obj)):
#            print(obj[j]['homeTeamName'])
#            print(obj[j]['awayTeamName'])
#            print(obj[j]['homeTeamScore'])
#            print(obj[j]['awayTeamScore'])

            sql = "SELECT COUNT(*) FROM football WHERE game_date = '" + src1['date'] + \
                  "' and homeTeam = '" + obj[j]['homeTeamName'] + "'"
#            print(sql)

            curs.execute(sql)

            result = curs.fetchall()
            for row_data in result:
                print(row_data[0])

                if row_data[0] == 0:
                    sql = "INSERT INTO `football` ( `game_date`, `homeTeam`, `homeScore`, \
                                `awayTeam`, `awayScore`, `league`) VALUES "
                    sql = sql + '(' + "'" + str(src1['date']) + "','" + str(obj[j]["homeTeamName"]) + "'," \
                          + obj[j]["homeTeamScore"] + ",'" + str(obj[j]["awayTeamName"]) + "'," \
                          + obj[j]["awayTeamScore"] + ", 'primera');"
                    curs.execute(sql)


conn.commit()

conn.close()

print('OK')