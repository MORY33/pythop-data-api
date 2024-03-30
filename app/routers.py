from fastapi import FastAPI, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from . import schemas, models
from .database import get_db

routes_router = APIRouter()

@routes_router.get("/routes", response_model=List[schemas.RouteSchema])
async def get_routes(db: Session = Depends(get_db)):
    routes = db.query(models.Route).all()
    return [schemas.RouteSchema.from_orm(route) for route in routes]

@routes_router.get("/routes/{route_id}", response_model=schemas.RouteWithPointsSchema)
async def get_route_by_id(route_id: int, db: Session = Depends(get_db)):
    route = db.query(models.Route).filter(models.Route.id == route_id).first()
    if route is None:
        raise HTTPException(status_code=404, detail="Route not found")
    return schemas.RouteWithPointsSchema.from_orm(route)
