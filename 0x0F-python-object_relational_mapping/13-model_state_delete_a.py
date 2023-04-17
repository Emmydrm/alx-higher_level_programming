#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # create connection to the database
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(sys.argv[1], sys.argv[2], sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # query the database to find states with "a" in their name
        states_with_a = session.query(State).filter(State.name.like('%a%')).all()

        # delete each state and commit the transaction
        for state in states_with_a:
            session.delete(state)
        session.commit()
