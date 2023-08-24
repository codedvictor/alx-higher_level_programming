#!/usr/bin/python3

"""a city class which inherit from base
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """class city with class attributes"""

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128),  nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
