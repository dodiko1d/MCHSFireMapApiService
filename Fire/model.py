""" Database Product Model. """

from sqlalchemy import Column, ForeignKey, Integer, String, CheckConstraint
from geoalchemy2 import Geography
from database import Base
from sqlalchemy.orm import relationship


class FirePoint(Base):
    __tablename__ = 'fire_point'

    id = Column(Integer, primary_key=True, index=True)
    coordinates = Column(Geography(geometry_type='POINT'))
    land_owner = Column(String)
    land_type = Column(String)
