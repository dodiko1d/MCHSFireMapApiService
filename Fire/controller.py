from sqlalchemy.orm import Session
from sqlalchemy import literal
from datetime import datetime
from . import model, schemas, helper

URL = 'http://maps.kosmosnimki.ru/rest/ver1/layers/F2840D287CD943C4B1122882C5B92565/search?query=%22DateTime%22%3E=%272020-08-07%27%20%20and%20%22DateTime%22%3C%272020-08-10%27%20&BorderFromLayer=78E56184F48149DF8A39BA81CA25A01E&BorderID=1&api_key=U26GSBBC7N&out_cs=EPSG:3395'

def time_logger(func):
    def wrapped(db: Session, fire_id: int, *args, **kwargs):
        result = func(*args, ** kwargs)
        fire = __get_firepoint_by_id(db=db, fire_id=fire_id)
        fire.update_time = datetime
        return result
    return wrapped


def overview_period(timestamp_1, timestamp_2):
    URL.replace(URL[URL.find('%27') + 3: URL.find('%27') + 13], timestamp_1)
    URL.replace(URL[URL.rfind('%27') - 12:URL.rfind('%27')], timestamp_2)
    return URL


def __get_fire_map(db: Session):
    web_data = helper.get_data()
    for i in range(len(web_data)):
        db_fire = helper.fire_from_api(i, web_data)
        db.add(db_fire)
        db.commit()
        db.refresh(db_fire)


def __get_firepoint_by_id(db: Session, fire_id: int):
    return db.query(model.FirePoint).filter(model.FirePoint.id == fire_id).first()


@time_logger
def fire_report(db: Session, fire: schemas.FirePoint):

    db_fire = model.FirePoint(
        id=fire.id,
        lat=fire.lat,
        long=fire.long,
        brightness=fire.brightness,
        probability=fire.probability,
        intensity=fire.intensity,
        fireType=fire.fireType,
        town=fire.town,
        dateTime=fire.dateTime,
        status=True,
        update_time=0
    )
    db.add(db_fire)
    db.commit()
    db.refresh(db_fire)


@time_logger
def fire_out(db: Session, fire_id: int):
    fire = __get_firepoint_by_id(db=db, fire_id=fire_id)
    fire.status = False
    return fire


@time_logger
def precipitation_start(db: Session, fire_id: int, volume: int):
    fire = __get_firepoint_by_id(db=db, fire_id=fire_id)
    fire.precipitation = volume
    return fire


@time_logger
def precipitation_stop(db: Session, fire_id: int):
    fire = __get_firepoint_by_id(db=db, fire_id=fire_id)
    fire.precipitation = 0
    return fire


@time_logger
def add_description(db: Session, fire_id: int, description: str):
    fire = __get_firepoint_by_id(db=db, fire_id=fire_id)
    fire.fire_description = description
    return fire



