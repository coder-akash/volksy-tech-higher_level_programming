#!/usr/bin/python3
''' task 6 '''
from sqlalchemy import Column, Interger, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class State:
    ''' class '''
    __tablename__ = states

    id = Column(Interger, primary_key=True)
    name = Column(String(128), nullable=False)
