from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
Base = declarative_base()


class Route(Base):
    __tablename__ = 'routes'
    id = Column(Integer, primary_key=True)
    route_id = Column(Integer, unique=True, nullable=False)
    from_port = Column(String, nullable=False)
    to_port = Column(String, nullable=False)
    leg_duration = Column(Integer, nullable=False)
    points = relationship("Point", backref="route")

class Point(Base):
    __tablename__ = 'points'
    id = Column(Integer, primary_key=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    timestamp = Column(BigInteger, nullable=False)
    speed = Column(Float, nullable=False)
    route_id = Column(Integer, ForeignKey('routes.route_id'), nullable=False)
