#-*- coding: utf-8 -*
import re
import requests as rq
import json
import calendar
import pandas
import pymysql
import sys


url = "https://sports.news.naver.com/wfootball/schedule/index.nhn?category=ligue1&year=2018&month=12"
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



start_date = p1 + p2 + '01'
end_date = p1 + p2 + str(period)

dt_index = pandas.date_range(start=start_date, end=end_date)
dt_list = dt_index.strftime("%Y%m%d").tolist()

#f = open('primera.txt', 'a')
conn = pymysql.connect(host='localhost', port=3306,  db='betman', user='root', password='syjm1998')
curs = conn.cursor()


for i in dt_list:
    len_list = len(aaa[str(i)])
    if len_list == 0:
        print("No data")
    else:
        for j in range(0, len_list):
            sql = "INSERT INTO `football` ( `game_date`, `homeTeam`, `homeScore`, \
            `awayTeam`, `awayScore`, `league`) VALUES "
            sql = sql + '(' + "'" + str(i) + "','" + str(aaa[str(i)][j]["homeTeamName"]) + "'," \
            + aaa[str(i)][j]["homeTeamScore"] + ",'" + str(aaa[str(i)][j]["awayTeamName"]) + "'," \
            + aaa[str(i)][j]["awayTeamScore"] + ", 'ligue1');"
            curs.execute(sql)
conn.commit()
conn.close()

print ("OK")