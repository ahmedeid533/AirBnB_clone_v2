#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """list of cities in state"""
            Cities = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    Cities.append(city)
            return Cities

