from datetime import datetime

from pydantic import BaseModel

class Product(BaseModel):
    prdno: int
    prdname: str
    contents: str
    price: int
    category: datetime
    stack: int
    img: str
    salepoint: float

    class Config:
        from_attributes = True

class NewProduct(BaseModel):
    prdname: str
    price: int
    contents: str
    stack: int
    salepoint: int

class GalAttach(BaseModel):
    pno: int
    prdno: int
    fname: str
    fsize: int

    class Config:
        from_attributes = True