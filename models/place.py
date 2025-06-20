#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    city = relationship("City", back_populates="places")
    user = relationship("User", back_populates="places")
    amenities  =relationship("Amenity", secondary="place_amenity", back_populates="places")

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        reviews = relationship("Review", back_populates="place", cascade="all, delete")
    else:
        @property
        def reviews(self):
            """Returns the list of Review instances with place_id equals to current Place.id (FileStorage only)"""
            from models import storage
            from models.review import Review
            review_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

place_amenity = Table("place_amenity", Base.metadata,
    Column("place_id", String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column("amenity_id", String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
    )