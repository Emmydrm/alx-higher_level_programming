#!/usr/bin/python3
"""
This script lists all states from the hbtn_0e_0_usa database that have a name
starting with the letter "N", sorted by ID.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    # Connecting to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])
    cur = bd.cursor()
    cur.execute("SELECT * FROM states WHERE (name LIKE 'N%') \
            ORDER BY id")
    rows = cur.fetchall()
    for item in rows
    print(item)
