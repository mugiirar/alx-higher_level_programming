#!/usr/bin/python3
"""
Defines a State model.
Inherits from SQLAlchemy Base and links to the MySQL table 'states'.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Represents a state for a MySQL database.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        id (sqlalchemy.Integer): The state's id.
        state_name (sqlalchemy.String): The state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, doc="The state's unique identifier.")
    state_name = Column(String(128), nullable=False, doc="The name of the state.")

    def __repr__(self):
        """
        Return a string representation of the State model.
        """
        return f"<State(id={self.id}, state_name={self.state_name})>"

