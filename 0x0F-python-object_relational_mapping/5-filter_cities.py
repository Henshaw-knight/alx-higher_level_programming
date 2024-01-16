#!/usr/bin/python3
"""Script that takes in the name of a states as an argument and lists all
cities of that state"""


import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    state_name = args[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                         passwd=args[2], database=args[3])

    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities INNER JOIN states
                ON cities.state_id = states.id WHERE states.name = '{}'
                ORDER BY cities.id ASC""".format(state_name))
    cities = cur.fetchall()

    for i in range(len(cities)):
        if (i != len(cities) - 1):
            print(cities[i][0], end=", ")
        else:
            print(cities[i][0])

    cur.close()
    db.close()
