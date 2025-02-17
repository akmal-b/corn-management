from sqlalchemy.orm import Session
from models import User, Location, Seller, Supply, Sale

def create_user(db: Session, username: str, role: str):
    user = User(username=username, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_location(db: Session, name: str, address: str):
    location = Location(name=name, address=address)
    db.add(location)
    db.commit()
    db.refresh(location)
    return location

def assign_seller(db: Session, user_id: int, location_id: int, salary: float):
    seller = Seller(user_id=user_id, location_id=location_id, salary=salary)
    db.add(seller)
    db.commit()
    db.refresh(seller)
    return seller

def add_supply(db: Session, location_id: int, quantity: int):
    supply = Supply(location_id=location_id, quantity=quantity)
    db.add(supply)
    db.commit()
    db.refresh(supply)
    return supply

def record_sale(db: Session, location_id: int, amount: float):
    sale = Sale(location_id=location_id, amount=amount)
    db.add(sale)
    db.commit()
    db.refresh(sale)
    return sale

def get_total_revenue(db: Session):
    sales = db.query(Sale).all()
    return sum(sale.amount for sale in sales)