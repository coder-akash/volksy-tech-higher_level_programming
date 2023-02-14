#!/usr/bin/python3
"""Task 14"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    ''' cities class '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False,
                      foreign_keys='states.id')
