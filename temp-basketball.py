import re
import requests as rq
import json
import calendar
import pandas
import pymysql
import sys
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen

#url = "https://sports.news.naver.com/wfootball/schedule/index.nhn?category=europa&year=2018&month=10"

html = urlopen("https://www.kbl.or.kr/schedule/today/list.asp")

soup = BeautifulSoup(html, 'html.parser')

data = soup.findAll("tbody")


print(len(data))


for i in range(0,len(data)):
    txt = data[i]
    home_list = txt.select('span.home')
    for j in range(0, len(home_list)):
        print(home_list[0])

    '''
    if td_hour == '-':
        pass
    else:
        td_date = txt.select('span.td_date')
        td_hour2 = txt.select('span.td_hour')
        team_lft = txt.select('span.team_lft')
        team_rgt = txt.select('span.team_rgt')
        td_score = txt.select('strong.td_score')

        print(type(td_date))
        print(td_date[0])
        print(td_hour2[0])
        print(team_lft[0])
        print(team_rgt[0])
        print(td_score[0])

#        print(td_date)
#        print(td_hour2)




    if td_hour == '-':
        pass
    else:
        print(txt.select('span.td_date'))
        print(td_hour)
        print(txt.select('span.team_lft'))
#        print(txt.select_one('span.td_score').text)
        print(txt.select('span.team_rgt'))

#    tag = soup.find("span", {"class":"td_hour"})
#    tag_title = tag.get_text()

#    print(data[i])


for tag in soup.findAll("span", {"class":"td_hour"}):
    print (tag)

#data = soup.find_all('span', class_='team_lft')

#print(data)


for tag in soup.select('div[class=sch_tb ]'):
    print (tag)

#matched = re.search(r'dailyScheduleListMap":(.*?;)', html, re.S)
matched = re.search(r'monthlyScheduleModel:(.*)', html)

tt = matched.group(1)
tt = tt[:-1]

data = json.loads(tt)

aaa = data["dailyScheduleListMap"]

print(aaa)
'''