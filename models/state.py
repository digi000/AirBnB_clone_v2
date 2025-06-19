#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    city = relationship("City", back_populates="state", cascade="all, delete")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """Returns the list of City instances with state_id equal to current State.id (FileStorage only)"""
            from models import storage
            from models.city import City
            return [city for city in storage.all(City).values() if city.state_id == self.id]