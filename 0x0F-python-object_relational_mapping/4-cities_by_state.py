#!/usr/bin/python3
"""
Lists all cities of the database hbtn_0e_4_usa, ordered by city id.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)
    
    with MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]) as db:
        cursor = db.cursor()

        
        query = """
            SELECT c.id, c.name, s.name
            FROM cities c
            INNER JOIN states s ON c.state_id = s.id
            ORDER BY c.id
        """
        cursor.execute(query)

        cities = cursor.fetchall()

        
        for city in cities:
            print(city)
