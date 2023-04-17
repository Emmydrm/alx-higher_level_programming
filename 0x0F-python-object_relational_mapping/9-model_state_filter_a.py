#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter 'a'
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Get the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the engine
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(mysql_username, mysql_password, database_name),
            pool_pre_ping=True)

    # Create the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects containing the letter "a"
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print the results
    for state in states:
        print("{}: {}".format(state.id, state.name))
