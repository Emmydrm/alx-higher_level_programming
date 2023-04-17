#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Set up connection to the database
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(username, password, db_name))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session object
    session = Session()

    # Query State objects, order by id
    query = session.query(State).order_by(State.id)

    # Print State objects
    for state in query.all():
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
