import pymysql
conn=pymysql.connect(host="localhost",user="root",passwd="",database="Extraction")
cur=conn.cursor()
cur.execute('update Employee set name="owais" where id=1')
i=cur.execute('select * from Employee')
for i in range(i):
	row=cur.fetchone()
	for y in row:
		print(y,end=" ")


		
