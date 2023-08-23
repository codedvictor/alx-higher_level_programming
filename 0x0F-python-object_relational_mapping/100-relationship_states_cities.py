#!/usr/bin/python3

"""
a script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""

from sqlalchemy import (create_engine)
from relationship_state import State, Base
from sqlalchemy.orm import sessionmaker, relationship
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    new_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                               format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)

    Base.metadata.create_all(new_engine)
    Session = sessionmaker(bind=new_engine)
    session = Session()

    n_state = State(name='California')
    n_city = City(name='San Franscisco', state=n_state)
    n_state.cities.append(n_city)

    session.add(n_state)
    session.add(n_city)
    session.commit()
