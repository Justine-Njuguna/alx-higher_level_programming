#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa

Usage: ./list_all_states.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys


def list_all_states(user, password, db_name):
    """Lists all states from the database hbtn_0e_0_usa.

    Args:
        user (str): Username for MySQL connection.
        password (str): Password for MySQL connection.
        db_name (str): Name of the database to connect to.
    """

    try:
        conn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=user,
                passwd=password,
                db=db_name
                )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cursor.fetchall()

        for row in rows:
            print(row[0], end="")  # Print state ID without newline
            print(":", row[1])  # Print state name with newline

        cursor.close()
        conn.close()

    except MySQLdb.Error as err:
        print(f"Error connecting to MySQL database: {err}")
        sys.exit(1)
