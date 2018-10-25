#-*- coding: utf-8 -*
import pymysql
import sys

conn = pymysql.connect(host='localhost', port=3306,  db='betman', user='root', password='syjm1998')
#input_file = sys.argv

f = open('primera.txt', 'r', encoding='utf8')
data = f.read()



curs = conn.cursor()
sql = "INSERT INTO `football` (`id`, `game-date`, `homeTeam`, `homeScore`, `awayTeam`, `awayScore`, `league`) VALUES "
sql = sql + data
curs.execute(sql)
print(sql)
conn.commit()

f.close()