from datetime import datetime

from sqlalchemy.orm import Session

from models.currency import Currency


def create_currency(db: Session, code: str, name: str, symbol: str, exchange_rate: float) -> Currency:
    """
    Event handler for creating new currencies in database
    :param db: Database session dependency.
    :param code: Currency's code
    :param name: Name of currency in polish language
    :param symbol: Currency's symbol # TODO
    :param exchange_rate: Exchange rate value
    :return: Currency from database
    """
    currency = Currency(code=code, name=name, symbol=symbol, exchange_rate=exchange_rate, updated_at=datetime.now())
    db.add(currency)
    db.commit()
    db.refresh(currency)
    return currency

def get_currency(db: Session, code: str) -> Currency:
    """
    Event handler for fetching currencies in database
    :param db: Database session dependency.
    :param code: Currency's code
    :return: Currency from database
    """
    return db.query(Currency).filter(Currency.code == code).first()

def update_exchange_rate(db: Session, code: str, new_rate: float) -> Currency:
    """
    Event handler for updating exchange rate for given currency in database
    :param code: Currency's code
    :param new_rate: New currency exchange rate to be updated
    :return: Conversion rate
    """
    currency = get_currency(db, code)
    if currency:
        currency.exchange_rate = new_rate
        db.commit()
        db.refresh(currency)
    return currency
