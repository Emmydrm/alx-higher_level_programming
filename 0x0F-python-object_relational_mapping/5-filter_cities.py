#!/usr/bin/python3
"""
Module that takes in the name of a state as an
argument and lists all cities of that state from
the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


def connectToDB():
    # Connecting to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name \
                 FROM cities \
                 INNER JOIN states \
                 ON cities.state_id = states.id \
                 WHERE states.name = %s \
                 ORDER BY cities.id", [sys.argv[4]])
    rows = cur.fetchall()
    cities = ""
    for item in rows[:-1]:
        cities += item[0] + ', '
    cities += rows[-1][0]
    print(cities)



if __name__ == "__main__":
    connectToDB()
