#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
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

    # Query the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Print the result or "Nothing" if the table is empty
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
