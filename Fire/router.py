from fastapi import APIRouter, Depends, HTTPException
from . import schemas, controller
from sqlalchemy.orm import Session
from database import SessionLocal


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


async def check_firepoint(fire_id: int, db: Session = Depends(get_db)):
    db_fire = controller.__get_firepoint_by_id(db, fire_id=fire_id)
    if not db_fire:
        raise HTTPException(status_code=400, detail='Firepoint with this id is not exist.')


@router.get('/get_fire_map/', summary='Получение карты пожаров.')
async def add_new_fire(fire: schemas.FirePoint, db: Session = Depends(get_db)):
    db_firemap = controller.get_fire_map(db)
    return db_firemap


@router.post('/add_new_fire/', summary='Добавление новой точки пожара.')
async def add_new_fire(fire: schemas.FirePoint, db: Session = Depends(get_db)):
    db_fire = controller.__get_firepoint_by_id(db, fire_id=fire.id)
    if db_fire:
        raise HTTPException(status_code=400, detail='Fire has been already added.')
    controller.fire_report(db=db, fire=fire)
    return {'status_code': '200'}


@router.post(
    '/remove_fire/{fire_id}',
    summary='Удаление точки пожара.',
    dependencies=[Depends(check_firepoint)]
)
async def remove_fire(fire_id: int, db: Session = Depends(get_db)):
    return controller.fire_out(db=db, fire_id=fire_id)
    # return {'status': 'Deleted'}


@router.post(
    '/precipitation_start/',
    summary='Осадки (объём)'
)
async def precipitation_start(fire_id: int, volume: int, db: Session = Depends(get_db)):
    return controller.precipitation_start(db=db, fire_id=fire_id, volume=volume)


@router.post(
    '/precipitation_stop/'
    summary='Отсутствие осадков'
)
async def precipitation_stop(fire_id: int, db: Session = Depends(get_db)):
    return controller.precipitation_stop(db=db, fire_id=fire_id)


@router.post(
    '/description/',
    summary='Дополнительное описание'
)
async def add_description(description: str, fire_id: int, db: Session = Depends(get_db)):
    return controller.add_description(db=db, fire_id=fire_id, description=description)
