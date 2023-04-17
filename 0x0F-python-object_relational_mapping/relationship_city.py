#!/usr/bin/env python3
"""
Contains the class definition of a City and an instance
Base = declarative_base()
"""
import sys
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
        Column, ForeignKey, Numeric
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
    City class inherits from Base
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
    state = relationship(State, back_populates="cities")

