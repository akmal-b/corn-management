from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import create_user, create_location, assign_seller, add_supply, record_sale, get_total_revenue

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user_route(username: str, role: str, db: Session = Depends(get_db)):
    return create_user(db, username, role)

@app.post("/locations/")
def create_location_route(name: str, address: str, db: Session = Depends(get_db)):
    return create_location(db, name, address)

@app.post("/sellers/")
def assign_seller_route(user_id: int, location_id: int, salary: float, db: Session = Depends(get_db)):
    return assign_seller(db, user_id, location_id, salary)

@app.post("/supplies/")
def add_supply_route(location_id: int, quantity: int, db: Session = Depends(get_db)):
    return add_supply(db, location_id, quantity)

@app.post("/sales/")
def record_sale_route(location_id: int, amount: float, db: Session = Depends(get_db)):
    return record_sale(db, location_id, amount)

@app.get("/reports/revenue/")
def get_revenue_route(db: Session = Depends(get_db)):
    return {"total_revenue": get_total_revenue(db)}
