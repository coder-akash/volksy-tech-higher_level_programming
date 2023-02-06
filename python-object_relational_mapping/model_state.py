#!/usr/bin/python3

from sqlalchemy import Column, Interger, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class State(Base):
    ''' class '''

    __tablename__ = 'states'
    id = Column(Interger, primary_key=True)
    name = Column(String(128), nullable=False)
