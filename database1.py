import sqlite3
conn=sqlite3.connect("emaildb.sqlite")
cur=conn.cursor()
cur.execute('drop table if exists count')
cur.execute('create table count (org text,counts integer)')
fname=input("Enter the file name:")
if len(fname)<3:
	fname="mbox.txt"
fh=open(fname)
for i in fh:
	if not i.startswith("From:"):
		continue
	i=i.rstrip()
	words=i.split()
	org=words[1]
	cur.execute('select counts from count where org=?',(org,))
	row=cur.fetchone()
	if row is None:
		cur.execute('insert into count (org,counts) values (?,1)',(org,))
	else:
		cur.execute('update count set counts=counts+1 where org=?',(org,))
	conn.commit()
sqlstr='select org,counts from count order by counts desc limit 10'
for row in cur.execute(sqlstr):
	print(str(row[0]),row[1])
cur.close()


