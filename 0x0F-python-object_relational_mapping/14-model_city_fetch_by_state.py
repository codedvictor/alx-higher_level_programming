#!/usr/bin/python3

"""
a script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""

from sqlalchemy import (create_engine)
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from model_city import City
from sys import argv


if __name__ == "__main__":
    new_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                               format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)

    Session = sessionmaker(bind=new_engine)
    session = Session()

    state_city = session.query(State, City).order_by(State.id).\
        filter(State.id == City.state_id).all()
    for state, city in state_city:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
