import pymysql
conn=pymysql.connect(host="localhost",user="root",passwd="",database="Extraction")
cur=conn.cursor()
l=cur.execute('select * from Employee')
print("sno.","name","email")
for i in range(l):
	row=cur.fetchone()
	for y in row:
		print(y,end=" ")
	print()


		
