# -*- coding: utf-8 -*
import pymysql

cus_cd = "FCEB6AFC"   #명륜진사갈비

conn = pymysql.connect(host='119.194.242.212', port=3306, db='starpos_r', user='root', password='syjm1998')
curs = conn.cursor()

conn2 = pymysql.connect(host='starpos-production-instance.ch1gq016d78x.ap-northeast-1.rds.amazonaws.com', port=3306, db='starpos', user='starpos', password='starpos2714')
curs2 = conn2.cursor()

sql = " select `payment_id`, `branch_id`, `operation_id`, `table_id`, \
        `status`, `credit_card`, `change`, `cash`, `point`, \
        `total`, Replace(`receipt_info`, \"\'\", '""'), `created_at` \
        from tb_payment where payment_id BETWEEN 17761 AND 17883 "
print(sql) 
curs.execute(sql)


result = curs.fetchall()

for row_data in result:
#    print(row_data[0])
#    print(row_data[1])
#    print(row_data[2])
#    sql2 = "INSERT INTO `tb_cus_branch_payment` ( `payment_id`, `branch_cd`, `cus_cd`, `operation_id`, `table_id`) values \
#            ("+str(row_data[0])+", '"+str(row_data[1])+"', '"+cus_cd+"', "+str(row_data[2])+", "+str(row_data[3])+" ); "
           

    sql2 = "INSERT INTO `tb_cus_branch_payment` ( `payment_id`, `branch_cd`, `cus_cd`, `operation_id`, `table_id`, \
		`status`, `credit_card`, `change`, `cash`, `point`, \
        `total`, `receipt_info`, `created_dt`, `mod_dt`, `reg_dt`) values \
		("+str(row_data[0])+", '"+str(row_data[1])+"', '"+cus_cd+"', "+str(row_data[2])+", "+str(row_data[3])+", \
		 "+str(row_data[4])+",  "+str(row_data[5])+", "+str(row_data[6])+", "+str(row_data[7])+", "+str(row_data[8])+", \
		 "+str(row_data[9])+", '"+str(row_data[10])+"', "+str(row_data[11])+", NOW(), NOW()  ); "
    curs2.execute(sql2)
    print(sql2) 

conn2.commit()

conn.close()
conn2.close()

print("OK")