#coding:utf-8
import pymysql

#create connect(host, user, passwd, db, charset, port) --> create cursor --> execute --> commit --> cursor close --> connect close

#create connection and cursor pointing to database
db = 'demo1'
conn = pymysql.connect(host="localhost", user="root", passwd="831219zzh", db=db, charset='utf8', port=3306)  
cursor = conn.cursor()

'''
#create database clause
cursor.execute("""create table if not exists t_sales2(
                id int primary key auto_increment not null,
                 nickName varchar(128) not null,
                  comment text not null,
                  saledate varchar(128) not null) engine=InnoDB default charset=utf8;""")
'''
##########################Insert Data######################
#use %s as placeholder
name = ['john', 'jerry','Jim', 'Zack']
#insert data into table
for i in name:
	cursor.execute("insert into t_sales2(nickName,comment,saledate) values(%s,%s,%s);", (i, "suitable", "2019-04-20"))

#prepare sql sentence first
name = ['john', 'jerry','Jim', 'Zack']
insert_sql = 'insert into t_sales2(nickName, comment, saledate) values(%s,%s,%s);'
for i in name:
	cursor.execute(insert_sql, (i, 'prepare sql first', '2020-03-05'))

#if the insertion number is equal to colums in table, we don't need to specify the column name
#cursor.execute("insert into t_sales2 values(%s, %s,%s,%s);", (200,'zzh', "suitable", "2019-04-20"))

#batch insertion use executemany method
info = [('gxg', 'good', '2019-02-03'),('zhen', 'nice','2020-02-02'),('zzt', 'great', '2018-02-09')]
row3 = cursor.executemany(insert_sql, info)


#####################update data############################
update_sql = "update t_sales2 set comment='white' where id=%s;"

#return affected row number, the second parameter is tuple, comma is needed if there is only one parameter
row2 = cursor.execute(update_sql,(1,))

####################select data############################
select_sql = "select * from t_sales2 where id>%s;"
#return affected row number
row3 = cursor.execute(select_sql,(1,))
print(row3, " rows were affected by selection!")

#select returns tuples in tuple. can fetch 1, n or all records
rows = cursor.fetchall()
row_one = cursor.fetchone()
row_n = cursor.fetch(5)
for i in rows:
	for j in i:
		print(j)

####################delete data###########################
delete_sql = "delete from t_sales2 where id=%s;"
#return affected row number
row4 = cursor.execute(delete_sql,(4,))

#########################commit data and Exit###############
#if don't commit, date won't be imported into database, be careful for large data insertion and commit on time.
conn.commit()
#close cursor
cursor.close()
#close connection
conn.close()
