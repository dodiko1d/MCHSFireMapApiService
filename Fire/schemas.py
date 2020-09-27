from typing import Optional
from pydantic import BaseModel


class FireSpot(BaseModel):
    id: int
    lat: float
    long: float
    brightness: float
    probability: float
    intensity: float
    fireType: float
    town: str
    dateTime: str
    owner: Optional[str] = None
    land_type: Optional[str] = None
    fuel: Optional[str] = None
    wind_direction: Optional[str] = None
    wind_speed: Optional[float] = None
    wind_gust: Optional[float] = None
    humidity: Optional[float] = None
    precipitation: Optional[float] = None
    description: Optional[str] = None
    area: Optional[float] = None
    status: bool
    update_time: str
