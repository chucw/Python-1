#-*- coding: utf-8 -*
import requests as rq
import re
import json
import calendar
import pandas

url = "https://sports.news.naver.com/kfootball/schedule/index.nhn?category=kleague&year=2020&month=05"

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

dt_index = pandas.date_range(start=start_date, end=end_date)
dt_list = dt_index.strftime("%Y%m%d").tolist()

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


            num = len(data_3["lineup"]["away"])
            num2 = len(data_3["lineup"]["home"])


            for k in range(0, num):
                if data_3['lineup']['away'][k]['posOrder'] == '-1':
                    pass
                else:
                    print (data_3["gameInfo"]["dateTime"], end='')
                    print(',', end='')
                    print (data_3["gameInfo"]["aName"], end='')
                    print(',', end='')
                    print(data_3["lineup"]["away"][k]["pName"], end='')               #플레이어 이름
                    print(',', end='')
                    print(data_3["lineup"]["away"][k]["pos"], end='')                 #포지션
                    print(',', end='')
                    print(data_3["lineup"]["away"][k]["posOrder"], end='')            #수비위치
                    print(',', end='')
                    if 'sTime' in data_3["lineup"]["away"][k]:
                        if data_3["lineup"]["away"][k]["sType"] == "in":
                            stime = 90 - int(data_3["lineup"]["away"][k]["sTime"])
                            print(stime, end='')
                            print(',', end='')                                            #출전시간
                        else:
                            print(data_3["lineup"]["away"][k]["sTime"], end='')
                            print(',', end='')                                            #출전시간
                    else:
                        print("90", end='')
                        print(',', end='')                                            #출전시간  
                    print(data_3["lineup"]["away"][k]["goal"])  


            for l in range(0, num2):
                if data_3['lineup']['home'][l]['posOrder'] == '-1':
                    pass
                else:
                    print (data_3["gameInfo"]["dateTime"], end='')
                    print(',', end='')
                    print (data_3["gameInfo"]["hName"], end='')
                    print(',', end='')
                    print(data_3["lineup"]["home"][l]["pName"], end='')               #플레이어 이름
                    print(',', end='')
                    print(data_3["lineup"]["home"][l]["pos"], end='')                 #포지션
                    print(',', end='')
                    print(data_3["lineup"]["home"][l]["posOrder"], end='')            #수비위치
                    print(',', end='')
                    if 'sTime' in data_3["lineup"]["home"][l]:
                        if data_3["lineup"]["home"][l]["sType"] == "in":
                            stime = 90 - int(data_3["lineup"]["home"][l]["sTime"])
                            print(stime, end='')
                            print(',', end='')                                            #출전시간
                        else:
                            print(data_3["lineup"]["home"][l]["sTime"], end='')
                            print(',', end='')                                            #출전시간
                    else:
                        print("90", end='')
                        print(',', end='')                                            #출전시간  
                    print(data_3["lineup"]["home"][l]["goal"])                      