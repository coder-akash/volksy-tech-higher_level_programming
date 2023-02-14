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
    name = sys.argv[4]
    data = s.query(State).filter_by(State.name = name).one()
    if data is None:
        print('Not found')
    else:
        print(data.id)

    s.close()
