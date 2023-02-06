#!/usr/bin/python3
# Lists all State objects from the database hbtn_0e_6_usa.
# Usage: ./7-model_state_fetch_all.py <mysql username> /
#                                     <mysql password> /
#                                     <database name>
import sys
from model_state import States
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]),pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    s = session()

    data  = s.query(State).order_by(State.id)

    for i in data:
        print('{}: {}'.format(i.id, i.name))
