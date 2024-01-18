#!/usr/bin/python3
"""Script that prints all City objects from the database"""


from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           username, password, database_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()

    results = session.query(State, City).filter(
             State.id == City.state_id).order_by(City.id).all()

    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
