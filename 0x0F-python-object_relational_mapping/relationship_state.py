#!/usr/bin/env python3
"""
Contains the class definition of a State and an instance
Base = declarative_base()
"""

import sys
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
        Column, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class State(Base):
    """
    State class inherits from Base
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship(City, back_populates="state", cascade="all, delete")
