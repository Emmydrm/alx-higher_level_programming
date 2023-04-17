#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    # Get MySQL credentials
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Start engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(user, password, db_name),
            pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a State object named "California"
    california = State(name="California")

    # Create a City object named "San Francisco" linked to "California"
    san_francisco = City(name="San Francisco", state=california)

    # Add the State and City objects to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the session to the database
    session.commit()

    # Close the session
    session.close()
