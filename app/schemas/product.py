from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Product(BaseModel):
    prdno: int
    prdname: str
    category: str
    img: str
    stack: int
    price: int
    salepoint: float
    regdate: datetime

    class Config:
        from_attributes = True


class NewProduct(BaseModel):
    prdname: str
    category: str
    img: Optional[str]
    stack: int
    price: int