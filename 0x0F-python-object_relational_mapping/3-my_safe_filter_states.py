#!/usr/bin/python3
"""Safer script of filter_states script"""


import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv

    db = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                         passwd=args[2], database=args[3])

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name = %s
            ORDER BY id ASC""", (sys.argv[4],))
    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
