#!/usr/bin/python3
""" Task 10"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    s = Session()

    query = s.query(State).all()
    # Create all name for states
    list_state = []
    for state in query:
        list_state.append(state.name)

    # Query
    query = s.query(State).\
        filter(State.name == "{}".format(sys.argv[4], )).first()

    # Conditions
    if sys.argv[4] not in list_state:
        print("Not found")
    else:
        print(query.id)

    # Close session
    s.close()
