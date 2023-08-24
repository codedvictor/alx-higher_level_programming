#!/usr/bin/python3

"""
a script that lists all City objects from the database hbtn_0e_101_usa
"""

from sqlalchemy import (create_engine)
from relationship_state import State, Base
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    new_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                               format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)

    Base.metadata.create_all(new_engine)
    Session = sessionmaker(bind=new_engine)
    session = Session()

    state_city = session.query(City).\
        order_by(City.id).all()
    for city in state_city:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
