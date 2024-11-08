from typing import List, Optional

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

import database
from database import get_db
from event_handlers import create_order, get_order, update_order_status
from helpers import _get_conversion_rate
from models import Order
from schemas import OrderCreate, OrderUpdate, OrderResponse

app = FastAPI()
database.set_db()


@app.post("/orders/", response_model=OrderResponse)
def create_order_endpoint(order: OrderCreate, db: Session = Depends(get_db)):
    new_order = create_order(db, order)
    return new_order


@app.get("/orders/{order_id}/", response_model=OrderResponse)
def get_order_endpoint(order_id: int, db: Session = Depends(get_db)):
    order = get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order_response = OrderResponse.model_validate(order)

    conversion_rate = _get_conversion_rate(order)
    if conversion_rate is None:
        raise HTTPException(status_code=400, detail="Currency not supported")

    order_response.converted_amount = round(order.total_amount * conversion_rate, 2)
    return order_response


@app.put("/orders/{order_id}/", response_model=OrderResponse)
def update_order_endpoint(order_id: int, order_update: OrderUpdate, db: Session = Depends(get_db)):
    updated_order = update_order_status(db, order_id, order_update.status)
    if not updated_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated_order

@app.get("/orders/", response_model=List[OrderResponse])
def list_orders(status: Optional[str] = None, db: Session = Depends(get_db)):
    """
    List all orders, optionally filtered by status.
    :param status: Optional order status to filter by (e.g., "pending", "shipped").
    :param db: Database session dependency.
    :return: A list of orders, optionally filtered by status.
    """
    query = db.query(Order)
    if status:
        query = query.filter(Order.status == status)
    return query.all()
