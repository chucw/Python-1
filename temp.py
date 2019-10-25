# -*- coding: utf-8 -*
import requests as rq
from bs4 import BeautifulSoup
import pymysql

url = "https://sports.news.naver.com/basketball/schedule/index.nhn?category=kbl&year=2019&month=10"
html = rq.get(url).text
soup = BeautifulSoup(html, 'html.parser')

t_div = soup.find_all("tr")

conn = pymysql.connect(host='localhost', port=3306, db='betman', user='root', password='syjm1998')
curs = conn.cursor()

for i in range(len(t_div)):
    if t_div[i].find('span', {'class': 'td_date'}):
        td_date = t_div[i].find('span', {'class': 'td_date'}).text

        a = len(td_date)
        b = td_date.find('.')
        if a == 9:
            month = td_date[0:2]
            dat = td_date[3:5]
        elif a == 8:
            if b == 1:
                month = '0' + td_date[0:b]
                dat = td_date[b + 1:b + 3]
            else:
                month = td_date[0:b]
                dat = '0' + td_date[b + 1:b + 2]
        else:
            month = '0' + td_date[0:b]
            dat = dat = '0' + td_date[b + 1]

    if t_div[i].find('span', {'class': 'td_hour'}):
        td_hour = t_div[i].find('span', {'class': 'td_hour'}).text
        if td_hour == '-':
            pass
        else:
            game_date = '2019' + month + dat
            hometeam = t_div[i].find('span', {'class': 'team_lft'}).text
            score = t_div[i].find('strong', {'class': 'td_score'}).text
            s_len = len(score)
            s_find = score.find(':')
            home_score = score[0:s_find]
            away_score = score[s_find + 1:]
            awayteam = t_div[i].find('span', {'class': 'team_rgt'}).text

            print(game_date, end=' ')
            print(hometeam, end=' ')
            print(home_score, end=' ')
            print(away_score, end=' ')
            print(awayteam)


print("OK")