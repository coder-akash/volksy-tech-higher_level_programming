#!/usr/bin/python3
"""Task 8"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    s = Session()

    data = s.query(State).order_by(State.id).first()

    if data is None:
        print("Nothing")
    else:
        print("{}: {}".format(data.id, data.name))

    s.close()
