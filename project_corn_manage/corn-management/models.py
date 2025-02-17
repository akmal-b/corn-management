from database import Base, engine
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    role = Column(String, default="seller")

class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)

class Seller(Base):
    __tablename__ = "sellers"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    location_id = Column(Integer, ForeignKey("locations.id"))
    salary = Column(Float, default=0.0)

class Supply(Base):
    __tablename__ = "supplies"
    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey("locations.id"))
    quantity = Column(Integer)
    delivery_date = Column(DateTime, default=datetime.utcnow)

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey("locations.id"))
    amount = Column(Float)
    date = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)