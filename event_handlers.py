from sqlalchemy.orm import Session
from models import Order, Currency
from schemas import OrderCreate

def create_order(db: Session, order: OrderCreate) -> Order:
    db_order = Order(
        customer_name=order.customer_name,
        total_amount=order.total_amount,
        currency=order.currency,
        status="pending"
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int) -> Order:
    return db.query(Order).filter(Order.id == order_id).first()

def update_order_status(db: Session, order_id: int, status: str) -> Order:
    order = db.query(Order).filter(Order.id == order_id).first()
    if order:
        order.status = status
        db.commit()
        db.refresh(order)
    return order

def get_orders(db: Session):
    return db.query(Order).all()





def create_currency(db: Session, code: str, name: str, symbol: str, exchange_rate: float):
    currency = Currency(code=code, name=name, symbol=symbol, exchange_rate=exchange_rate)
    db.add(currency)
    db.commit()
    db.refresh(currency)
    return currency

def get_currency(db: Session, code: str):
    return db.query(Currency).filter(Currency.code == code).first()

def update_exchange_rate(db: Session, code: str, new_rate: float):
    currency = get_currency(db, code)
    if currency:
        currency.exchange_rate = new_rate
        db.commit()
        db.refresh(currency)
    return currency
