#!/usr/bin/python3
"""Write script that changes the name of a State object with id = 2
from the database"""


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
    state = session.query(State).get(2)

    if state:
        state.name = "New Mexico"
    session.commit()
    session.close()
