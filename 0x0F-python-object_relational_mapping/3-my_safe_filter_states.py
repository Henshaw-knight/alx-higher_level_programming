#!/usr/bin/python3
"""Safer script of filter_states script"""


import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv

    safer_state_arg = (args[4].split(';'))[0]

    db = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                         passwd=args[2], database=args[3])

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC""".format(safer_state_arg))
    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
