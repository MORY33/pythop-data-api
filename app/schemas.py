from typing import List
from pydantic import BaseModel

class PointSchema(BaseModel):
    longitude: float
    latitude: float
    timestamp: int
    speed: float

    class Config:
        orm_mode = True




class RouteSchema(BaseModel):
    route_id: int
    from_port: str
    to_port: str
    leg_duration: int

    class Config:
        orm_mode = True

class RouteWithPointsSchema(RouteSchema):
    points: List[PointSchema]

    class Config:
        orm_mode = True
