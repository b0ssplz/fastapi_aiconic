import requests
from sqlalchemy.orm import Session

import config
from event_handlers.currency_events import update_exchange_rate, create_currency, get_currency
from models.order import Order


def get_conversion_rate(db: Session, order: Order) -> float:
    """
    Retrieve response from NBP API and save conversion rates
    :param db: Database session dependency.
    :param order: Order data
    :return: Conversion rate
    """
    order_currency = order.currency_code

    nbp_response = requests.get(config.NBP_API_URL).json()
    rates = next(iter(nbp_response)).get('rates')
    for rate in rates:
        code = rate.get('code')
        name = rate.get('currency')
        if code == order_currency:
            conversion_rate = rate.get('mid')
            reversed_conversion_rate = 1 / conversion_rate
            currency = get_currency(db, code)
            if not currency:
                create_currency(db, code, name, 'symbol_test', reversed_conversion_rate)
            update_exchange_rate(db, code, reversed_conversion_rate)
            return reversed_conversion_rate
