from datetime import datetime
from typing import Optional, Union

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


class PrdAttach(BaseModel):
    prdno: int
    img1: Optional[str]
    img2: Optional[str]
    img3: Optional[str]
    img4: Optional[str]

    class Config:
        from_attributes = True


class NewData(BaseModel):
    prdname: str
    category: str
    img1: Optional[str]
    img2: Optional[str]
    img3: Optional[str]
    img4: Optional[str]
    stack: int
    price: int
    contents: str


class NewProduct(BaseModel):
    prdname: str
    category: str
    stack: int
    price: int
    contents: str


class RowData(BaseModel):
    prdno: int
    prdname: str
    stack: int
    price: int
    salepoint: Union[int, float]




