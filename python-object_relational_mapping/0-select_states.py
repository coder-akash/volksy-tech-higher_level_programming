#!/usr/bin/python3
import MySQLdb as mysql


''' main program '''
conn = mysql.connect(host='localhost', user='root',passwd='',database='hbtn_0e_0_usa')
cur = conn.cursor()
cur.execute('SELECT * FROM states ORDER BY id')
data =  cur.fetchall()
for i in data:
    print(i)
