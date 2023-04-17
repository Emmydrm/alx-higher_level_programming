#!/usr/bin/python3
"""
ORM Script
"""
import sys
import sqlalchemy
~from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
        Column, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Creates the State class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
