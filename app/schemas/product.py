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


class NewProduct(BaseModel):
    prdname: str
    category: str
    stack: int
    price: int


class RowData(BaseModel):
    data1: str
    data2: str
    data3: str
    data4: str
    data5: str
    data6: str
    data7: str
    data8: str




