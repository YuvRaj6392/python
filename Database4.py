import pymysql
conn=pymysql.connect(host="localhost",user="root",passwd="",database="CourseraDatabase")
cur=conn.cursor()
cur.execute('drop table if exists Ages')
cur.execute('create table Ages (name varchar(128),age integer)')
cur.execute('insert into Ages (name,age) values ("Benjamin",26)')
cur.execute('insert into Ages (name,age) values ("Roray",31)')
cur.execute('insert into Ages (name,age) values ("Oisin",30)')
cur.execute('insert into Ages (name,age) values ("Salahudin",13)')
cur.execute('insert into Ages (name,age) values ("Sofian",20)')
cur.execute('select hex("name || age") as X order by X')
row=cur.fetchone()
for i in row:
	print(i)




