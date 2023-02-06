#!/usr/bin/python3
''' task 1 '''
import MySQLdb as mysql
import sys


if __name__ == "__main__":
    conn = mysql.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    data = cur.fetchall()
    for i in data:
        if i[1][0] == 'N':
            print(i)
