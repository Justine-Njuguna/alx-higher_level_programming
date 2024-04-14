#!/usr/bin/python3


import sys
"""
Lists all states starting with 'N' from the database hbtn_0e_0_usa
"""

import MySQLdb


def list_states_by_name(user, password, db_name):
    """Lists all states from the database hbtn_0e_0_usa starting with 'N'.

    Args:
        user (str): Username for MySQL connection.
        password (str): Password for MySQL connection.
        db_name (str): Name of the database to connect to.
    """

    try:
        # Connect to MySQL server
        conn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=user,
                passwd=password,
                db=db_name
                )
        cursor = conn.cursor()

        # Execute query with LIKE operator for names starting with 'N'
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(query)

        # Fetch and print results
        rows = cursor.fetchall()
        for row in rows:
            print(row[0], end="")  # Print state ID without newline
            print(":", row[1])  # Print state name with newline

    except MySQLdb.Error as err:
        print(f"Error connecting to MySQL database: {err}")
        sys.exit(1)

    finally:
        # Close the connection (optional, handled by garbage collection)
        if conn:
            conn.close()


if __name__ == "__main__":
    # No argument validation needed (as per task instructions)
    list_states_by_name(sys.argv[1], sys.argv[2], sys.argv[3])
