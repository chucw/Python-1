#-*- coding: utf-8 -*
import requests as rq
import re
import json
import calendar
import pandas
import pymysql

url = "https://sports.news.naver.com/kfootball/schedule/index.nhn?category=kleague&year=2018&month=11"

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
#end_date = p1 + p2 + str(period)
end_date = p1 + p2 + '06'

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
            matched_2 = re.search(r'relayDataUrl:(.*)', html_2)
            tt_2 = matched_2.group(1)
            tt_2 = tt_2[2:]
            tt_2 = tt_2[:-1]

            html_3 = rq.get(tt_2).text

            data_3 = json.loads(html_3)


            num = len(data_3["lineup"]["home"])
            num2 = len(data_3["lineup"]["away"])


            for k in range(0, num):
#            for k in range(0, 2):
                if data_3['lineup']['home'][k]['posOrder'] == '-1':
                    pass
                else:
                    if 'sTime' in data_3["lineup"]["home"][k]:
                        if data_3["lineup"]["home"][k]["sType"] == "in":
                            stime = 90 - int(data_3["lineup"]["home"][k]["sTime"])
                        else:
                            stime = int(data_3["lineup"]["home"][k]["sTime"])
                    else:
                        stime = 90

                    sql = "INSERT INTO football_member (league, game_date, teamName, \
                    type, shirtNumber, player, position, posorder, stime, goal) VALUES " \
                    '(' + "'kleague'" + ",'" + str(data_3["gameInfo"]["dateTime"]) + "', '" \
                    + str(data_3["gameInfo"]["hName"]) + "', 'home', " \
                    + data_3["lineup"]["home"][k]["shirtNumber"] + ", '" + str(data_3["lineup"]["home"][k]["pName"]) \
                    + "', '" + str(data_3["lineup"]["home"][k]["pos"]) + "', '" \
                    + str(data_3["lineup"]["home"][k]["posOrder"]) + "', " + str(stime) \
                    + ", " + data_3["lineup"]["home"][k]["goal"] + ");"              
                    curs.execute(sql)
#                    print(sql)
          

            for l in range(0, num2):
                if data_3['lineup']['away'][l]['posOrder'] == '-1':
                    pass
                else:
                    if 'sTime' in data_3["lineup"]["away"][l]:
                        if data_3["lineup"]["away"][l]["sType"] == "in":
                            stime = 90 - int(data_3["lineup"]["away"][l]["sTime"])
                        else:
                            stime = int(data_3["lineup"]["away"][l]["sTime"])
                    else:
                        stime = 90

                    sql = "INSERT INTO football_member (league, game_date, teamName,                        \
                    type, shirtNumber, player, position, posorder, stime, goal) VALUES "                    \
                    '(' + "'kleague'" + ",'" + str(data_3["gameInfo"]["dateTime"]) + "', '"                   \
                    + str(data_3["gameInfo"]["aName"]) + "', 'away', " \
                    + data_3["lineup"]["away"][l]["shirtNumber"] + ", '" + str(data_3["lineup"]["away"][l]["pName"]) \
                    + "', '" + str(data_3["lineup"]["away"][l]["pos"]) + "', '"                               \
                    + str(data_3["lineup"]["away"][l]["posOrder"]) + "', " + str(stime)                       \
                    + ", " + data_3["lineup"]["away"][l]["goal"] + ");"                         
                    curs.execute(sql)

conn.commit()

conn.close()

print ("OK")                                        