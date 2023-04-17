#!/usr/bin/python3
"""
Module that lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connecting to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
            ORDER BY id".format(sys.argv[4]))

    rows = cur.fetchall()
    for item in rows:
        print(item)
