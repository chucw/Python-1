#-*- coding: utf-8 -*
import requests as rq
import re
from bs4 import BeautifulSoup
import pymysql
import json

url = "https://sports.news.naver.com/basketball/schedule/index.nhn?category=kbl&year=2018&month=10"
html = rq.get(url).text
soup = BeautifulSoup(html, 'html.parser')

t_div = soup.find_all("tr")

for i in range(len(t_div)):
    if t_div[i].find('span',{'class':'td_date'}):
        td_date = t_div[i].find('span',{'class':'td_date'}).text

        a = len(td_date)
        b = td_date.find('.')
        if a == 9:
            month = td_date[0:2]
            dat = td_date[3:5]
        elif a == 8:
            if b == 1:
                month = '0' + td_date[0:b]
                dat = td_date[b+1:b+3]
            else:
                month = td_date[0:b]
                dat = '0' + td_date[b+1:b+2]
        else:
            month = '0' + td_date[0:b]
            dat = dat = '0' + td_date[b+1]

    
    if t_div[i].find('span',{'class':'td_hour'}):
        td_hour = t_div[i].find('span',{'class':'td_hour'}).text
        if td_hour == '-':
            pass
        else:
            game_date = '2018' + month + dat
            link = t_div[i].find('a')
                       
            url2 = 'https://sports.news.naver.com/' + link.get('href')
#            여기까지는 정상적으로 동작함
            html2 = rq.get(url2).text
            matched = re.search(r'initKblLive(.*)', html2)

            tt = matched.group(1)
            tt = tt[2:-3]
            print(tt)
            
            html3 = rq.get(tt).text
#            여기도 통과
            data = json.loads(html3)

            game_date = data["game_date"]
            game_text = data["player_avg_record"]["game"]
            print(game_text)

            for k in game_text.keys():
                if type(game_text[k]) == dict:
                    tt = game_text[k]
                    for j in tt.keys():
                        mem_str = tt[j]
                        mem_str = mem_str.split(',')
                        mem_name = mem_str[0]
                        mem_position = mem_str[1]
                        mem_team_code = mem_str[2]
                        mem_back_num = mem_str[3]
                        mem_paly_min = mem_str[4]
                        mem_fg = mem_str[6]
                        mem_fg_a = mem_str[7]
                        mem_off_reb = mem_str[14]
                        mem_def_reb = mem_str[15]
                        mem_assist = mem_str[16]
                        mem_score = mem_str[22]
                        
                        print(game_date, ':', end=' ')
                        print(mem_name,', ',end=' ')
                        print(mem_position,', ',end=' ')
                        print(mem_team_code,', ',end=' ')
                        print(mem_back_num,', ',end=' ')
                        print(mem_paly_min,', ',end=' ')
                        print(mem_fg,', ',end=' ')
                        print(mem_fg_a,', ',end=' ')
                        print(mem_off_reb,', ',end=' ') 
                        print(mem_def_reb,', ',end=' ')
                        print(mem_assist,', ',end=' ')
                        print(mem_score)
    else:
        pass

print ("OK")