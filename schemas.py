from pydantic import BaseModel
from models import OrderStatus

class OrderCreate(BaseModel):
    customer_name: str
    total_amount: float
    currency: str
    status: OrderStatus

class OrderUpdate(BaseModel):
    status: OrderStatus


class OrderResponse(BaseModel):
    id: int
    customer_name: str
    total_amount: float
    currency: str
    status: OrderStatus
    converted_amount: float = None

    class Config:
        from_attributes = True
