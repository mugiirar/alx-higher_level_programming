#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

def main():
    if len(sys.argv) != 4:
        print("Usage: ./script_name.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{database_name}",
                               pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        for city, state in session.query(City, State) \
                                  .filter(City.state_id == State.id) \
                                  .order_by(City.id):
            print(f"{state.name}: ({city.id}) {city.name}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

