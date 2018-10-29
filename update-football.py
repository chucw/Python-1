#-*- coding: utf-8 -*
import re
import requests as rq
import json
import calendar
import pandas
import pymysql
import sys


url = "https://sports.news.naver.com/wfootball/schedule/index.nhn?category=ligue1&year=2018&month=10"
html = rq.get(url).text

# print (html)

#matched = re.search(r'dailyScheduleListMap":(.*?;)', html, re.S)
matched = re.search(r'monthlyScheduleModel:(.*)', html)

tt = matched.group(1)
tt = tt[:-1]

data = json.loads(tt)

aaa = data["dailyScheduleListMap"]

p1 = data["year"]
p2 = data["month"]
#print(p1, p2)
#print(type(p1), type(p2))

period = calendar.monthrange(int(p1), int(p2))[1]



start_date = p1 + p2 + '26'
end_date = p1 + p2 + str(period)

dt_index = pandas.date_range(start=start_date, end=end_date)
dt_list = dt_index.strftime("%Y%m%d").tolist()

#f = open('primera.txt', 'a')
conn = pymysql.connect(host='localhost', port=3306,  db='betman', user='root', password='syjm1998')
curs = conn.cursor()


for i in dt_list:
    len_list = len(aaa[str(i)])
    if len_list == 0:
        pass
    else:
        for j in range(0, len_list):
            sql = "UPDATE football SET homeScore = "
            sql = sql + aaa[str(i)][j]["homeTeamScore"]
            sql = sql + " WHERE homeTeam = '" + str(aaa[str(i)][j]["homeTeamName"]) + "'"
            sql = sql + " AND game_date = '" + str(i) + "'"
            curs.execute(sql)
            
            sql2 = "UPDATE football SET awayScore = "
            sql2 = sql2 + aaa[str(i)][j]["awayTeamScore"]
            sql2 = sql2 + " WHERE awayTeam = '" + str(aaa[str(i)][j]["awayTeamName"]) + "'"
            sql2 = sql2 + " AND game_date = '" + str(i) +"'"
            curs.execute(sql2)
conn.commit()            
conn.close()

print ("OK")