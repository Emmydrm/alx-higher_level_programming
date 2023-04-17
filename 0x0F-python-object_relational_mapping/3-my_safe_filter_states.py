#!/usr/bin/env python3
"""
Script that takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument (safe from MySQL injections).
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]

    # Connect to database
    db = MySQLdb.connect(host='localhost',
            user=username,
            passwd=password,
            db=database,
            port=3306)

    # Create cursor and execute parameterized query
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", (search,))

    # Fetch and print results
    for row in cur.fetchall():
        print(row)

    # Close cursor and database
    cur.close()
    db.close()
