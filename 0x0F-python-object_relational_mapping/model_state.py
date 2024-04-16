#!/usr/bin/python3
"""
Module containing the State class and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of the declarative base
Base = declarative_base()


class State(Base):
    """
    State class to represent the states table
    """
    __tablename__ = 'states'

    # Define columns
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
