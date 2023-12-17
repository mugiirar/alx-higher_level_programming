#!/usr/bin/python3
"""
Lists all State objects that contain the letter a
from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

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

        for state in session.query(State).order_by(State.id):
            if "a" in state.state_name:
                print(f"{state.id}: {state.state_name}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

