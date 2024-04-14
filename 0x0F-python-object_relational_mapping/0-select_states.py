#!/usr/bin/python3
import MySQLdb
import sys

def main():
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    try:
        conn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=mysql_username,
                passwd=mysql_password,
                db=database_name
                )
        cur = conn.cursor()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    # Execute SQL query
    try:
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        
        # Fetch and display results
        for row in cur.fetchall():
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close cursor and connection
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
