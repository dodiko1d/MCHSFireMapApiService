""" Database Fire point Model. """

from sqlalchemy import Column, ForeignKey, Integer, String, CheckConstraint, Float, Boolean
from geoalchemy2 import Geography
from database import Base
from sqlalchemy.orm import relationship


class FirePoint(Base):
    __tablename__ = 'fire_point'

    id = Column(Integer, primary_key=True, index=True)
    coordinates = Column(Geography(geometry_type='POINT'))
    owner = Column(String)
    land_type = Column(String)
    fuel = Column(String)
    wind_direction = Column(String)
    wind_speed = Column(Float)
    wind_gust = Column(Float)
    humidity = Column(Float)
    precipitation = Column(Float)
    description = Column(String)
    area = Column(Float)
    status = Column(Boolean)
    update_time = Column()
