#!/usr/bin/python3
''' script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa: '''
import MySQLdb as mysql


if __name__ == "__main__":
    conn = mysql.connect(host='localhost', user='root', passwd='root',
                         database=hbtn_0e_0_usa)
    cur = conn.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE N% ORDER BY id')
    data =  cur.fetchall()
    for i in data:
        print(i)
