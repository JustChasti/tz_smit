from pydantic import BaseModel, validator
from datetime import date


class ProductModel(BaseModel):
    product_date: date = date.today()
    product_type: str = 'Other'
    cost: float = 0
