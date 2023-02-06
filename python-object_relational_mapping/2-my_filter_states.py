#!/usr/bin/python3
''' task 2 '''
import MySQLdb as mysql
import sys


if __name__ == "__main__":
    conn = mysql.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    names = sys.argv[4:]
    cur = conn.cursor()
    q = 'SELECT * FROM states ORDER BY id'
    cur.execute(q)
    data = cur.fetchall()
    for i in data:
        if i in names:
            print('{}'.format(i))
