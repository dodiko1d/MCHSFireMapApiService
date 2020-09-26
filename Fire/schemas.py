from typing import Optional
from pydantic import BaseModel


class FireSpot(BaseModel):
    id: int
    coordinates: Geography(geometry_type='POINT')
    owner: str
    land_type: str
    fuel: str
    wind_direction: str
    wind_speed: float
    wind_gust: float
    humidity: float
    precipitation: float
    description: str
    area: float
    status: bool
    update_time: str
