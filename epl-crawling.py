<<<<<<< HEAD
#-*- coding: utf-8 -*
import re
import requests as rq
import json
import calendar
import pandas


url = "https://sports.news.naver.com/wfootball/schedule/index.nhn?category=epl&year=2018&month=10"
html = rq.get(url).text

#matched = re.search(r'dailyScheduleListMap":(.*?;)', html, re.S)
matched = re.search(r'monthlyScheduleModel:(.*)', html)

tt = matched.group(1)
tt = tt[:-1]

data = json.loads(tt)

aaa = data["dailyScheduleListMap"]



p1 = data["year"]
p2 = data["month"]


period = calendar.monthrange(int(p1), int(p2))[1]



start_date = p1 + p2 + '01'
end_date = p1 + p2 + str(period)

dt_index = pandas.date_range(start=start_date, end=end_date)
dt_list = dt_index.strftime("%Y%m%d").tolist()

sn = 45

f = open('epl.txt', 'a', encoding='utf8')

for i in dt_list:
    len_list = len(aaa[str(i)])
    if len_list == 0:
        pass
    else:
        for j in range(0, len_list-1):
            sn = sn + 1
            f.write('(')
            f.write(str(sn))
            f.write(",'")
            f.write(str(i))
            f.write("','")
            f.write(aaa[str(i)][j]["homeTeamName"])  
            f.write("',")   
            f.write(aaa[str(i)][j]["homeTeamScore"])
            f.write(',')   
            f.write(aaa[str(i)][j]["awayTeamScore"])
            f.write(",'")   
            f.write(aaa[str(i)][j]["awayTeamName"])
            f.write("', 'epl'),")               
            f.write('\n')

f.close()