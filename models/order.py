from enum import Enum

from sqlalchemy import Column, Integer, String, Float, Enum as SQLAlchemyEnum, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class OrderStatus(str, Enum):
    pending = "pending"
    shipped = "shipped"
    delivered = "delivered"

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, index=True)
    total_amount = Column(Float)
    status = Column(SQLAlchemyEnum(OrderStatus), nullable=False)
    currency_code = Column(String, ForeignKey("currencies.code"), nullable=False)
    currency = relationship("Currency", back_populates="orders")
