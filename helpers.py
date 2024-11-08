import requests

import config
from models import Order


def _get_conversion_rate(order: Order) -> dict:
    order_currency = order.currency

    nbp_response = requests.get(config.NBP_API_URL).json()
    rates = next(iter(nbp_response)).get('rates')
    for rate in rates:
        if rate.get('code') == order_currency:
            conversion_rate = rate.get('mid')
            reversed_conversion_rate = 1 / conversion_rate
            return reversed_conversion_rate
