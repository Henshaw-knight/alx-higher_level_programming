#!/usr/bin/python3
"""Script that lists all states with a name starting with 'N' from the
database"""


import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=args[1], passwd=args[2], database=args[3])

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE
                name LIKE 'N%' ORDER BY states.id ASC""")
    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
