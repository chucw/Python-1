#-*- coding: utf-8 -*
import requests as rq
import re
import json
import calendar
import pandas
import pymysql

url = "https://sports.news.naver.com/wfootball/schedule/index.nhn?category=ligue1&year=2018&month=11"

html = rq.get(url).text

matched = re.search(r'monthlyScheduleModel:(.*)', html)

tt = matched.group(1)
tt = tt[:-1]
#print(tt)

data = json.loads(tt)

#print(data)

aaa = data["dailyScheduleListMap"]

p1 = data["year"]
p2 = data["month"]

period = calendar.monthrange(int(p1), int(p2))[1]

start_date = p1 + p2 + '01'
end_date = p1 + p2 + str(period)
#end_date = p1 + p2 + '07'

dt_index = pandas.date_range(start=start_date, end=end_date)
dt_list = dt_index.strftime("%Y%m%d").tolist()

conn = pymysql.connect(host='localhost', port=3306,  db='betman', user='root', password='syjm1998')
curs = conn.cursor()


for i in dt_list:
    len_list = len(aaa[str(i)])
    if len_list == 0:
        pass
    else:
        for j in range(0, len_list):
            html_2 = rq.get(aaa[str(i)][j]["textRelayURI"]).text
            matched_2 = re.search(r'initWorldfootballLive(.*)', html_2)

            tt_2 = matched_2.group(1)
            tt_2 = tt_2[2:]
            tt_2 = tt_2[:-2]
            
            html_3 = rq.get(tt_2).text
            
            data_3 = json.loads(html_3)

            away_text = data_3["lineup"]["away"]
            home_text = data_3["lineup"]["home"]


            for k in home_text.keys():
                if data_3["date"] == "":
                    pass
                else:
                    if (len(data_3["lineup"]["home"][k]["substitute"])) > 0:
                        if data_3["lineup"]["home"][k]["substitute"]["type"] == "in":
                            sTime = data_3["lineup"]["home"][k]["substitute"]["time"]
                        else:
                            sTime = 90 - int(data_3["lineup"]["home"][k]["substitute"]["time"])                    
                    else:
                        sTime = 90
                    

                    sql = "INSERT INTO football_member (league, game_date, teamName, \
                    type, shirtNumber, player, position, posorder, stime, goal) VALUES " \
                    '(' + "'ligue1'" + ",'" + str(data_3["date"]) + "', '" \
                    + str(data_3["basic_info"]["home_team_name"]) + "', 'home', " \
                    + data_3["lineup"]["home"][k]["shirt_number"] + ", '"  \
                    + str(data_3["lineup"]["home"][k]["player_name"]) \
                    + "', '" + str(data_3["lineup"]["home"][k]["position"]) + "', '" \
                    + str(data_3["lineup"]["home"][k]["position_order"]) + "', " + str(sTime) \
                    + ", " + data_3["lineup"]["home"][k]["goal"] + ");"              
                    curs.execute(sql)



            for l in away_text.keys():
                if data_3["date"] == "":
                    pass
                else:
                    if (len(data_3["lineup"]["away"][l]["substitute"])) > 0:
                        if data_3["lineup"]["away"][l]["substitute"]["type"] == "in":
                            sTime = data_3["lineup"]["away"][l]["substitute"]["time"]
                        else:
                            sTime = 90 - int(data_3["lineup"]["away"][l]["substitute"]["time"])                    
                    else:
                        sTime = 90
                    

                    sql = "INSERT INTO football_member (league, game_date, teamName, \
                    type, shirtNumber, player, position, posorder, stime, goal) VALUES " \
                    '(' + "'ligue1'" + ",'" + str(data_3["date"]) + "', '" \
                    + str(data_3["basic_info"]["away_team_name"]) + "', 'away', " \
                    + data_3["lineup"]["away"][l]["shirt_number"] + ", '" + str(data_3["lineup"]["away"][l]["player_name"]) \
                    + "', '" + str(data_3["lineup"]["away"][l]["position"]) + "', '" \
                    + str(data_3["lineup"]["away"][l]["position_order"]) + "', " + str(sTime) \
                    + ", " + data_3["lineup"]["away"][l]["goal"] + ");"              
                    curs.execute(sql)


conn.commit()

conn.close()

print ("OK")