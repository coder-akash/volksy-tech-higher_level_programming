#!/usr/bin/python3
''' task 4'''
import MySQLdb as mysql
import sys


if __name__ == "__main__":
    conn = mysql.connect(user=sys.argv[1], passwd=sys.argv[2],
                         database=sys.argv[3])
    cur = conn.cursor()
    q = 'SELECT cities.id, cities.name, states.name FROM cities 
    INNER JOIN states ON cities.state_id = states.id ORDER BY id'
    cur.execute(q)
    data = cur.fetchall()
    for i in data:
        print(i)
