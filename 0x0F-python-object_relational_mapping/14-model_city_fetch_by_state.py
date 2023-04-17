#!/usr/bin/python3
""" Lists all City objects from the database hbtn_0e_14_usa """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # set up connection to the database
    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(db_user, db_pass, db_name),
            pool_pre_ping=True)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    # perform the query to get all cities and states
    rows = session.query(City, State).join(State).order_by(City.id).all()

    # print the results
    for city, state in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
