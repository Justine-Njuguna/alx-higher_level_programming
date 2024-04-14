#!/usr/bin/python3
"""
Lists all states matching the provided name from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb


if __name__ == "__main__":
    # No argument validation needed (as per task instructions)
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=password,
            db=db_name
            )
    cursor = conn.cursor()

    # Build query with LIKE operator for wildcard search
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch and print results
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row[0], end="")  # Print state ID without newline
            print(":", row[1])  # Print state name with newline
    else:
        print("Not found")

    # Close the connection
    conn.close()
