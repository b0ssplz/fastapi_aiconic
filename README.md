# fastapi_aiconic

API has 4 main endpoint to interact with, for documentation use swagger - http://127.0.0.1:8000/docs.

External API of NBP is used here for fetching exchange rates- https://api.nbp.pl/api

Used NBP API endpoint: https://api.nbp.pl/api/exchangerates/tables/A/

Example data:

```
<ArrayOfExchangeRatesTable>
<ExchangeRatesTable>
<Table>A</Table>
<No>214/A/NBP/2024</No>
<EffectiveDate>2024-11-04</EffectiveDate>
<Rates>
<Rate>
<Currency>bat (Tajlandia)</Currency>
<Code>THB</Code>
<Mid>0.1183</Mid>
</Rate>
<Rate>
<Currency>dolar amerykański</Currency>
<Code>USD</Code>
<Mid>3.9869</Mid>
</Rate>
<Rate>
<Currency>dolar australijski</Currency>
<Code>AUD</Code>
<Mid>2.6290</Mid>
</Rate>
</Rates
</ExchangeRatesTable>
</ArrayOfExchangeRatesTable>
```



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

