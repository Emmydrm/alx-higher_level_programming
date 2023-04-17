#!/usr/bin/env python3
"""lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Set up the MySQL connection
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(username, password, db_name), pool_pre_ping=True)
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the database for all States and their associated Cities
    results = session.query(State).order_by(State.id).all()

    # Print out the results
    for state in results:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    # Close the session
    session.close()
