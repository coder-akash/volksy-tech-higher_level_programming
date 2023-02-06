#!/usr/bin/python3
''' task 5 '''
import MySQLdb as mysql
import sys


if __name__ == "__main__":
    conn = mysql.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    name = sys.argv[4]
    cur = conn.cursor()
    cur.execute('''select cities.name from cities inner join states
    on cities.state_id = states.id where states.name = '{}' '''.format(name))
    data = cur.fetchall()
    if len(data) > 0:
        for i in range(len(data)):
            if i == len(data) - 1:
                print(data[i][0])
            else:
                print(data[i][0], end=', ')
    else:
        print()
