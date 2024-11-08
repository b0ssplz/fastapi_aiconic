from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.orm import relationship

from database import Base


class Currency(Base):
    __tablename__ = 'currencies'

    code = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    symbol = Column(String)
    exchange_rate = Column(Float, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    orders = relationship("Order", back_populates="currency")