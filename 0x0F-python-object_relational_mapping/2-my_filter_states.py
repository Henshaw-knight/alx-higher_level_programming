#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the
states table of the database that matches the argument"""


import MySQLdb
import sys


if __name__ == "__main__":
    args = sys.argv

    db = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                         passwd=args[2], database=args[3])

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name = '{}'
                ORDER BY states.id ASC""".format(args[4]))
    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
