#!/usr/bin/python3

"""
a script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""

from sqlalchemy import (create_engine)
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    new_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                               format(sys.argv[1], argv[2], argv[3], argv[4]),
                               pool_pre_ping=True)

    Session = sessionmaker(bind=new_engine)
    session = Session()
    state = session.query(State).order_by(State.id).\
        filter(State.name == argv[4]).first()
    if not state:
        print('Not found')
    else:
        print(state.id)
