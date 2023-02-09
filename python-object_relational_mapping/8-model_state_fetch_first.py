#!/usr/bin/python3
""" task 8 """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    s = session()
    data = s.query(State).order_by(State.id).one()
    print('{}: {}'.format(data.id data.name)
