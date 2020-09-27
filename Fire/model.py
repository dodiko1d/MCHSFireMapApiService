""" Database Fire point Model. """

from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from database import Base


class FirePoint(Base):
    __tablename__ = 'fire_point'

    id = Column(Integer, primary_key=True)
    lat = Column(Float)
    long = Column(Float)
    brightness = Column(Float)
    probability = Column(Float)
    intensity = Column(Float)
    fireType = Column(Integer)
    town = Column(String)
    dateTime = Column(String)
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
    update_time = Column(DateTime)
