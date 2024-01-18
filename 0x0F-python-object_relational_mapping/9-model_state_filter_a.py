#!/usr/bin/python3
"""Script that lists all State objects that contain the letter a from
the database"""


from model_state import Base, State
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

    states_with_a = session.query(State).filter(
                    State.name.contains('a')
                    ).order_by(State.id).all()
    if states_with_a:
        for state in states_with_a:
            print("{}: {}".format(state.id, state.name))

    session.close()
