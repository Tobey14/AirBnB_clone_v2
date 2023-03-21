#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = 'cities'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
    else:
        state_id = ""
        name = ""