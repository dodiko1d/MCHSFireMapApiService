from fastapi import FastAPI

# Application separated routers.
from Fire.router import router as fire_router

# Database models.
import Fire.model as fire_model

# Database settings.
from database import engine
from database import SessionLocal


# Creating models.
fire_model.Base.metadata.create_all(bind=engine)

# Application instance.
app = FastAPI()


# Connecting separated routers.

app.include_router(
    fire_router,
    prefix='/fire',
    tags=['Fire'],
    responses={404: {'description': 'Not found'}}
)