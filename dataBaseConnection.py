import pymysql
conn=pymysql.connect(host="localhost",user="root",passwd="",database="Extraction")
cursor=conn.cursor()
if cursor:
	print("success")
else:
	print("failed to connect")