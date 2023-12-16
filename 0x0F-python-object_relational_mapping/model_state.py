#!/usr/bin/python3
"""
Defines a city
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    """Represents a city in a MySQL database.

    Attributes:
        id (int): The city's id.
        name (str): The city's name.
        state_id (int): The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)  # Adjusted the length for flexibility
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
