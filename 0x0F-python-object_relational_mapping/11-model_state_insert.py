#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

def main():
    if len(sys.argv) != 4:
        print("Usage: ./script_name.py <mysql username> <mysql password> <database name>")
        return

    try:
        engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
                               pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        louisiana = State(name="Louisiana")
        session.add(louisiana)
        session.commit()

        print(f"Added state: {louisiana.name} with id: {louisiana.id}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if session:
            session.close()

if __name__ == "__main__":
    main()
