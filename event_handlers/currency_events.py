from datetime import datetime

from sqlalchemy.orm import Session

from models.currency import Currency


def create_currency(db: Session, code: str, name: str, symbol: str, exchange_rate: float) -> Currency:
    """
    List all orders, optionally filtered by status.
    :param db: Database session dependency.
    :param order: Database session dependency.
    :return: Conversion rate
    """
    currency = Currency(code=code, name=name, symbol=symbol, exchange_rate=exchange_rate, updated_at=datetime.now())
    db.add(currency)
    db.commit()
    db.refresh(currency)
    return currency

def get_currency(db: Session, code: str) -> Currency:
    """
    List all orders, optionally filtered by status.
    :param db: Database session dependency.
    :param order: Database session dependency.
    :return: Conversion rate
    """
    return db.query(Currency).filter(Currency.code == code).first()

def update_exchange_rate(db: Session, code: str, new_rate: float) -> Currency:
    """
    List all orders, optionally filtered by status.
    :param db: Database session dependency.
    :param order: Database session dependency.
    :return: Conversion rate
    """
    currency = get_currency(db, code)
    if currency:
        currency.exchange_rate = new_rate
        db.commit()
        db.refresh(currency)
    return currency
