#!/usr/bin/python3
"""Lists cities of a given state"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3],
                           charset="utf8")

    cur = conn.cursor()

    cur.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """, (argv[4], ))

    cities = cur.fetchall()

    print(", ".join([city[0] for city in cities]))

    cur.close()
    conn.close()
