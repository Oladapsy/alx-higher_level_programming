#!/usr/bin/python3
""" a Python file similar to model_state.py named model_city.py
"""
from sqlalchemy import Column, Foreignkey, String, Integer
from model_state import State, Base

class City(Base):
    """ inherits from Base imported from model_state """
    __tablename__ = "Cities"

    id = Column(Integer, Primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, Foreignkey("state.id"), nullable=False)
