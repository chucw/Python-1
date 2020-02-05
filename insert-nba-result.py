#-*- coding: utf-8 -*
import requests as rq
from bs4 import BeautifulSoup
import pyodbc

url = "https://sports.news.naver.com/basketball/schedule/index.nhn?category=nba&year=2020&month=02"
html = rq.get(url).text
soup = BeautifulSoup(html, 'html.parser')

t_div = soup.find_all("tr")

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\sheep\Documents\betman.accdb;')
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

            #            print(game_date, end=' ')
            #            print(hometeam, end=' ')
            #            print(home_score, end=' ')
            #            print(away_score, end=' ')
            #            print(awayteam)

            if home_score == 'V':
                pass
            else:

                sql = "SELECT COUNT(*) FROM basketball WHERE game_date = '" + str(game_date) + "'"
                sql = sql + " and homeTeam = '" + str(hometeam) + "'"
                sql = sql + " and awayTeam = '" + str(awayteam) + "'"

                curs.execute(sql)

                result = curs.fetchall()
                for row_data in result:
                    if row_data[0] == 0:
                        sql = "INSERT INTO `basketball` ( `game_date`, `homeTeam`, `homeScore`, \
                                        `awayTeam`, `awayScore`, `league`) VALUES "
                        sql = sql + '(' + "'" + str(game_date) + "','" + str(awayteam) + "'," \
                              + away_score + ",'" + str(hometeam) + "', " + home_score + ", 'NBA');"
                        curs.execute(sql)
                    #                    print(sql)
                    else:
                        sql = "UPDATE `basketball` SET "
                        sql = sql + "homeScore = " + away_score
                        sql = sql + ", awayScore = " + home_score
                        sql = sql + " where game_date = '" + str(game_date) + "'"
                        sql = sql + " and homeTeam = '" + str(awayteam) + "'"
                        sql = sql + " and awayTeam = '" + str(hometeam) + "'"
                        sql = sql + " and league = 'NBA'"
                        curs.execute(sql)

conn.commit()
conn.close()

print("OK")