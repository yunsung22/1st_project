from datetime import datetime

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


class NewMember(BaseModel):
    userid: str
    passwd: str
    name: str
    email: str