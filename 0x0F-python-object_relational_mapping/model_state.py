#!/usr/bin/python3

"""
Defines a State class which inherit from base
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


mymeta = MetaData()
Base = declarative_base(metadata=mymeta)


class State(Base):
    """State class with one MySQL table
    """

    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128),  nullable=False)
