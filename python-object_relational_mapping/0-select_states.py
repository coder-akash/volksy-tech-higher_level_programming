#!/usr/bin/python3
'''script that lists all states from the database hbtn_0e_0_usa:'''
import MySQLdb as mysql
import sys


if __name__ == "__main__":
    conn = mysql.connect(user=sys.argv[1], passwd=sys.argv[2],
                         database=sys.argv[3])
    cur = conn.cursor()
    cur.execute('SELECT * FROM states ORDER BY id')
    data = cur.fetchall()
    for i in data:
        print(i)
