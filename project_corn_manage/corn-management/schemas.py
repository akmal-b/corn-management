from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    username: str
    role: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    class Config:
        from_attributes = True

class LocationBase(BaseModel):
    name: str
    address: str

class LocationCreate(LocationBase):
    pass

class LocationResponse(LocationBase):
    id: int
    class Config:
        from_attributes = True

class SellerBase(BaseModel):
    user_id: int
    location_id: int
    salary: float

class SellerCreate(SellerBase):
    pass

class SellerResponse(SellerBase):
    id: int
    class Config:
        from_attributes = True

class SupplyBase(BaseModel):
    location_id: int
    quantity: int
    delivery_date: Optional[datetime] = datetime.utcnow()

class SupplyCreate(SupplyBase):
    pass

class SupplyResponse(SupplyBase):
    id: int
    class Config:
        from_attributes = True

class SaleBase(BaseModel):
    location_id: int
    amount: float
    date: Optional[datetime] = datetime.utcnow()

class SaleCreate(SaleBase):
    pass

class SaleResponse(SaleBase):
    id: int
    class Config:
        from_attributes = True
