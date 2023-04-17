#!/usr/bin/python3
"""
Start link class to table in database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a connection to the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session object to begin transactions
    session = Session()

    # Add a new state to the database
    new_state = State(name='California')
    session.add(new_state)
    session.commit()

    # Query the database and print all states
    states = session.query(State).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
