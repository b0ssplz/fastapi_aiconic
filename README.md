# fastapi_aiconic

API has 4 main endpoint to interact with, for documentation use swagger - http://127.0.0.1:8000/docs.

External API of NBP is used here for fetching exchange rates- https://api.nbp.pl/api

Database consists of two tables, Order and Currency. Currency table is used as a helper table to store currency data fetched from NBP API.

Example json data for POST:
```
{
    "customer_name": "Andrzej Kowalski",
    "total_amount": 100.0,
    "currency_code": "EUR",
    "status": "pending"
}
```

