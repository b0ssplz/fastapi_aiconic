from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from database import Base

from enum import Enum

class OrderStatus(str, Enum):
    pending = "pending"
    shipped = "shipped"
    delivered = "delivered"

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, index=True)
    total_amount = Column(Float)
    # currency = Column(String)
    status = Column(Enum(OrderStatus), nullable=False)  # Use Enum here
    currency = relationship("Currency", backref="orders")

class Currency(Base):
    __tablename__ = 'currencies'

    code = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    symbol = Column(String)
    exchange_rate = Column(Float, nullable=False)
    updated_at = Column(DateTime, nullable=False)
