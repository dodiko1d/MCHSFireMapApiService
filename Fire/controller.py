from sqlalchemy.orm import Session
from sqlalchemy import literal


from . import model, schemas


def __get_fire_map(db: Session):
    return db.query(model.FirePoint).all()


def __get_firepoint_by_id(db: Session, fire_id: int):
    return db.query(model.FirePoint).filter(model.FirePoint.id == fire_id).first()


def fire_report(db: Session, fire: schemas.FireSpot):

    db_fire = model.FirePoint(
        id=fire.id,
        coordinates=fire.coordinates,
        owner=fire.owner,
        land_type=fire.land_type,
        fuel=fire.fuel,
        wind=fire.wind_direction,
        wind_speed=fire.wind_speed,
        wind_gust=fire.wind_gust,
        humidity=fire.humidity,
        precipitation=fire.precipitation,
        description=fire.description,
        area=fire.area,
        status=True,
        update_time=fire.update_time
    )
    db.add(db_fire)
    db.commit()
    db.refresh(db_fire)
    return {'status_code': '200'}


def fire_out(db: Session, fire_id: int):
    fire = __get_firepoint_by_id(db=db, fire_id=fire_id)
    fire.status = False
    return fire


def precipitation_start(db: Session, fire_id: int, volume: int):
    fire = __get_firepoint_by_id(db=db, fire_id=fire_id)
    fire.precipitation = volume
    return fire


def precipitation_stop(db: Session, fire_id: int):
    fire = __get_firepoint_by_id(db=db, fire_id=fire_id)
    fire.precipitation = 0
    return fire


def add_description(db: Session, fire_id: int, description: str):
    fire = __get_firepoint_by_id(db=db, fire_id=fire_id)
    fire.fire_description = description
    return fire



