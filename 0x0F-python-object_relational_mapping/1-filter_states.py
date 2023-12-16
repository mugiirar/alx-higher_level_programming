#!/usr/bin/python3
"""
Lists all states with a name
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    # Use a context manager to ensure proper handling of resources
    with MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]) as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM `states` WHERE `name` LIKE 'N%' ORDER BY `id`")
        states_starting_with_n = cursor.fetchall()

        # Use a more explicit loop for better readability
        for state in states_starting_with_n:
            print(state)

