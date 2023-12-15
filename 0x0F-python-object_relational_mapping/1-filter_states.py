#!/usr/bin/python
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    # Use a context manager to ensure proper handling of resources
    with MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        rows = cursor.fetchall()
        
        for row in rows:
            print (row)
