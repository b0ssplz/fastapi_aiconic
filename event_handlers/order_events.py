from typing import Type

from sqlalchemy.orm import Session

from models.order import Order
from schemas import OrderCreate


def create_order(db: Session, order: OrderCreate) -> Order:
    """
    List all orders, optionally filtered by status.
    :param db: Database session dependency.
    :param order: Database session dependency.
    :return: Conversion rate
    """
    db_order = Order(
        customer_name=order.customer_name,
        total_amount=order.total_amount,
        currency_code=order.currency_code,
        status="pending"
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int) -> Order:
    """
    List all orders, optionally filtered by status.
    :param db: Database session dependency.
    :param order: Database session dependency.
    :return: Conversion rate
    """
    return db.query(Order).filter(Order.id == order_id).first()

def update_order_status(db: Session, order_id: int, status: str) -> Order:
    """
    List all orders, optionally filtered by status.
    :param db: Database session dependency.
    :param order: Database session dependency.
    :return: Conversion rate
    """
    order = db.query(Order).filter(Order.id == order_id).first()
    if order:
        order.status = status
        db.commit()
        db.refresh(order)
    return order

def get_orders(db: Session) -> list[Type[Order]]:
    """
    List all orders, optionally filtered by status.
    :param db: Database session dependency.
    :param order: Database session dependency.
    :return: Conversion rate
    """
    return db.query(Order).all()
