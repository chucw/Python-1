# -*- coding: utf-8 -*
import pymysql

cus_cd = "FD1B1707"

conn = pymysql.connect(host='119.194.242.212', port=3306, db='starpos', user='root', password='syjm1998')
curs = conn.cursor()

conn2 = pymysql.connect(host='starpos-production-instance.ch1gq016d78x.ap-northeast-1.rds.amazonaws.com', port=3306, db='distribution', user='starpos', password='starpos2714')
curs2 = conn2.cursor()

sql = " select * from trandeta where trandeta_id > 1956 "
curs.execute(sql)

result = curs.fetchall()

for row_data in result:
#    print(row_data[0])
#    print(row_data[1])
#    print(row_data[2])
#    sql2 = "INSERT INTO `trandeta` ( `cus_cd`, `branch_cd`, `posno`, `ydate`, `recno`) values "
#    sql2 = sql2 + " ('"+cus_cd+"', '"+str(row_data[1])+"', '"+str(row_data[2])+"', '"+str(row_data[3])+"', "+str(row_data[4])+"); "

    sql2 = "INSERT INTO `trandeta` ( `cus_cd`, `branch_cd`, `posno`, `ydate`, `recno`, \
		`seqno`, `ytime`, `ptable`, `sflag`, `ucode`, \
        `bcode`, `gcode`, `ccode`, `sname`, `stand`, \
        `iprce`, `aprce`, `quant`, `amout`, `saldt`, `other`,  \
        `salso`, `optio`, `etc`, `cs_cd`, \
        `sdate`, `oflag`, `pcheck`, `psave`, `jbang`) Values \
		('"+cus_cd+"', '"+str(row_data[1])+"', '"+str(row_data[2])+"', '"+str(row_data[3])+"', "+str(row_data[4])+", \
		 "+str(row_data[5])+",  '"+str(row_data[6])+"', "+str(row_data[7])+", '"+str(row_data[8])+"', '"+str(row_data[9])+"', \
		 '"+str(row_data[10])+"', '"+str(row_data[11])+"', '"+str(row_data[12])+"', '"+str(row_data[13])+"', '"+str(row_data[14])+"', \
		 "+str(row_data[15])+", "+str(row_data[16])+", "+str(row_data[17])+",  "+str(row_data[18])+", "+str(row_data[19])+", \
		 "+str(row_data[20])+", '"+str(row_data[21])+"', '"+str(row_data[22])+"', '"+str(row_data[23])+"', '"+str(row_data[24])+"', \
		 '"+str(row_data[25])+"', '"+str(row_data[26])+"', '"+str(row_data[27])+"', "+str(row_data[28])+", '"+str(row_data[29])+"' ); "

    curs2.execute(sql2)
    print(sql2)

conn2.commit()

conn.close()
conn2.close()

print("OK")