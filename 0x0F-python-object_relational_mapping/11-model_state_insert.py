#!/usr/bin/python3

"""
a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""

from sqlalchemy import (create_engine)
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    new_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                               format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)

    Session = sessionmaker(bind=new_engine)
    session = Session()

    state = session.add(State.name='Louisiana')
    session.commit()
    print(state.id)
