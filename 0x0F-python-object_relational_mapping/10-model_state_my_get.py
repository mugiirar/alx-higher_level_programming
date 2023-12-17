#!/usr/bin/python3
"""
prints the State object with the name passed as argument from a database
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

def main():
    if len(argv) != 5:
        print("Usage: ./script_name.py <mysql username> <mysql password> "
              "<database name> <state name>")
        return

    try:
        eng = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
        Base.metadata.create_all(eng)
        Session = sessionmaker(bind=eng)
        session = Session()

        state = session.query(State).filter_by(name=argv[4]).first()

        if state:
            print(f"{state.id}")
        else:
            print("Not found")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if session:
            session.close()

if __name__ == "__main__":
    main()

