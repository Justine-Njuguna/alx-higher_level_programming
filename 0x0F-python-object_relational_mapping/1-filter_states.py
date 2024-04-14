#!/usr/bin/python3
""" lists all states beginning with N """

import sys
import MySQLdb


def connect_to_database(user, password, database):
    """Connects to the MySQL database.
    """
    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=user,
                passwd=password,
                db=database
                )
        cs = db.cursor()
        return db, cs
    except MySQLdb.Error as err:
        print(f"Error connecting to MySQL database: {err}")
        sys.exit(1)


def fetch_states(cursor):
    """Fetches states starting with 'N' from the database.
    """
    cursor.execute("
    SELECT * FROM `states`
    WHERE name LIKE 'N%'
    ORDER BY id ASC"
    )
    return cursor.fetchall()


def print_states(states):
    """Prints each state information on a separate line.
    """
    for state in states:
        print(state)


def main():
    """Main function to connect, fetch, and print states."""

    if __name__ == "__main__":
        db, cs = connect_to_database(sys.argv[1], sys.argv[2], sys.argv[3])
        states = fetch_states(cs)
        print_states(states)
        cs.close()
        db.close()
    if __name__ == "__main__":
        main()
