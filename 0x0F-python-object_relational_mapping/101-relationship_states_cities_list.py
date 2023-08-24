#!/usr/bin/python3

"""
a script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_6_usa
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

    state_city = session.query(State).outerjoin(City).\
        order_by(State.id, City.id).all()
    for state in state_city:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
