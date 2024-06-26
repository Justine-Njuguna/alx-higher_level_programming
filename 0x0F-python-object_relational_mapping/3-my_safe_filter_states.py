#!/usr/bin/python3
""" Displays in the states table where name matches the args - SQL Injection"""


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost',
        port=3306
    )
    cursor = db.cursor()

    query = """
        SELECT *
        FROM `states`
        WHERE BINARY `name` = '{}'
    """.format(sys.argv[4])

    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
