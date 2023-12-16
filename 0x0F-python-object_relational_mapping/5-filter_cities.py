#!/usr/bin/python3
"""
Displays all cities of a given state
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name> <state name searched>".format(sys.argv[0]))
        sys.exit(1)
    with MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]) as db:
        cursor = db.cursor()

        query = """
            SELECT c.id, c.name, s.name
            FROM cities c
            INNER JOIN states s ON c.state_id = s.id
            WHERE s.name = %s
            ORDER BY c.id
        """
        cursor.execute(query, (sys.argv[4],))

        cities_in_state = cursor.fetchall()

        city_names = [city[1] for city in cities_in_state]
        print(", ".join(city_names))

