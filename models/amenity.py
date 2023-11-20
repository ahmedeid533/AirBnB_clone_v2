#!/usr/bin/python3
"""import modules for amenity"""
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.base_model import BaseModel



class Amenity(BaseModel, Base):
    """enjoy boy"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
