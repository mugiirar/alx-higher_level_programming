#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name> <state name searched>".format(sys.argv[0]))
        sys.exit(1)


    with MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]) as db:
        cursor = db.cursor()

        
        query = "SELECT * FROM `states` WHERE BINARY `name` = %s"
        cursor.execute(query, (sys.argv[4],))

        states_matching_name = cursor.fetchall()

        for state in states_matching_name:
            print(state)

