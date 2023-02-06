#!/usr/bin/python3
''' task 2 '''
import MySQLdb as mysql
import sys


if __name__ == "__main__":
    conn = mysql.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    names = sys.argv[4:]
    cur = conn.cursor()
    cur.execute('SELECT * FROM states WHERE name IN {} ORDER BY id'.format(tuple(names)))
    data = cur.fetchall()
    for i in data:
        print(i)
